#!/home/pi/robotEnv/bin python 

import sys
from threading import Thread
import multiprocessing
import argparse
import json
import os.path
import pathlib2 as pathlib
import os
import struct
import subprocess
import logging
import time
import random
import pvporcupine
import pyaudio
import google.oauth2.credentials
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file
from google.assistant.library.device_helpers import register_device
from indicator import robotIndicator

#from rightHand import grip, open
#from leftHand import grip, open
#from hand import handshake, handup
#from mobility import Forward, Backward, Stop, Left, Right, rightCircle, leftCircle

from move import speakingModeOn
from talk import say
import yaml 

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))

with open('{}/src/conversation.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    custom_conversation = yaml.load(conf, Loader=yaml.FullLoader)

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

WARNING_NOT_REGISTERED = ""

if os.path.isfile('/tmp/robot.log'):
    os.system('sudo rm /tmp/robot.log')

logging.root.handlers = []
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG , filename='/tmp/robot.log')
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))


mutestopbutton=True



access_key = "RZk+UIYxsDmjiYXb4ctA0dx8SOfMxpFcm0wlGUz2WWg6rOwCmTf7nA=="
picovoice_models=['/home/pi/Robot-Niko/Extras/hey-niko.ppn']
wakeword_length=1

numQuestion=len(custom_conversation['Conversation']['Question'])
numAnswer=len(custom_conversation['Conversation']['Answer'])
# numInput=len(custom_conversation['Action']['Input'])
# numOutput=len(custom_conversation['Action']['Output'])

speakingModeOn()

class Myassistant():
    def __init__(self):
        self.can_start_conversation=False
        self.assistant=None
        self._library_path = pvporcupine.LIBRARY_PATH
        self._model_path = pvporcupine.MODEL_PATH
        self._keyword_paths = picovoice_models
        self._input_device_index = None
        self._sensitivities = [0.5]*wakeword_length
        self.mutestatus=False
        self.singleresposne=False
        self.singledetectedrespone=''
        self.t1 = Thread(target=self.picovoice_run)

    def process_event(self,event):
        print()
        print('Now event is ', event)
        print()
        if event.type == EventType.ON_MUTED_CHANGED:
            self.mutestatus=event.args["is_muted"]


        if event.type == EventType.ON_START_FINISHED:
            self.can_start_conversation = True
            if os.path.isfile("{}/.mute".format(USER_PATH)):
                robotIndicator('mute')

            os.system("amixer -D pulse sset Master 0%")
            self.assistant.set_mic_mute(True)
            time.sleep(0.9)
            os.system("amixer -D pulse sset Master 100%")

            self.t1.start()


        if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
            subprocess.Popen(["aplay", "{}/audio-files/listening.wav".format(ROOT_PATH)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.can_start_conversation = False
            robotIndicator('listening')


        if (event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT or event.type == EventType.ON_NO_RESPONSE):
            self.can_start_conversation = True
            robotIndicator('off')

            os.system("amixer -D pulse sset Master 0%")
            self.assistant.set_mic_mute(True)
            time.sleep(0.9)
            os.system("amixer -D pulse sset Master 100%")
            if os.path.isfile("{}/.mute".format(USER_PATH)):
                robotIndicator('mute')


        if (event.type == EventType.ON_RESPONDING_STARTED and event.args and not event.args['is_error_response']):
            robotIndicator('speaking')

        if event.type == EventType.ON_RESPONDING_FINISHED:
            robotIndicator('off')


        if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
            robotIndicator('off')
            if self.singleresposne:
                self.assistant.stop_conversation()
                self.singledetectedresponse= event.args["text"]
            else:
                usrcmd=event.args["text"]
                self.custom_command(usrcmd)


        if event.type == EventType.ON_RENDER_RESPONSE:
            robotIndicator('off')


        if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and event.args and not event.args['with_follow_on_turn']):
            self.can_start_conversation = True
            robotIndicator('off')

            os.system("amixer -D pulse sset Master 0%")
            self.assistant.set_mic_mute(True)
            time.sleep(0.9)
            os.system("amixer -D pulse sset Master 100%")
            if os.path.isfile("{}/.mute".format(USER_PATH)):
                robotIndicator('mute')


        if event.type == EventType.ON_DEVICE_ACTION:
            for command, params in event.actions:
                print('Do command', command, 'with params', str(params))


        if event.type == EventType.ON_RENDER_RESPONSE:
            onlineAnswer= event.args["text"]
            print('online answer is  ', onlineAnswer)
            print('length of answer = ', len(onlineAnswer))



    def register_device(self,project_id, credentials, device_model_id, device_id):
        base_url = '/'.join([DEVICE_API_URL, 'projects', project_id, 'devices'])
        device_url = '/'.join([base_url, device_id])
        session = google.auth.transport.requests.AuthorizedSession(credentials)
        r = session.get(device_url)
        print(device_url, r.status_code)
        if r.status_code == 404:
            print('Registering....')
            r = session.post(base_url, data=json.dumps({
                'id': device_id,
                'model_id': device_model_id,
                'client_type': 'SDK_LIBRARY'
            }))
            if r.status_code != 200:
                raise Exception('failed to register device: ' + r.text)
            print('\rDevice registered.')


    def detected(self):
        if self.can_start_conversation == True:
            if self.mutestatus:
                os.system("amixer -D pulse sset Master 0%")
                self.assistant.set_mic_mute(False)
                time.sleep(1)
                os.system("amixer -D pulse sset Master 100%")
                self.assistant.start_conversation()
            if not self.mutestatus:
                self.assistant.start_conversation()
            print('Robot is listening....')


    def picovoice_run(self):
        keywords = list()
        for x in self._keyword_paths:
            keywords.append(os.path.basename(x).replace('.ppn', '').split('_')[0])

        porcupine = None
        pa = None
        audio_stream = None
        try:
            porcupine = pvporcupine.create(
                access_key=access_key,
                library_path=self._library_path,
                model_path=self._model_path,
                keyword_paths=self._keyword_paths,
                sensitivities=self._sensitivities)

            pa = pyaudio.PyAudio()

            audio_stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length,
                input_device_index=self._input_device_index)

            while True:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
                result = porcupine.process(pcm)
                if result >= 0:
                    self.detected()

        except KeyboardInterrupt:
            print('Stopping ...')
        finally:
            if porcupine is not None:
                porcupine.delete()
            if audio_stream is not None:
                audio_stream.close()
            if pa is not None:
                pa.terminate()


    def single_user_response(self,prompt):
        self.singledetectedresponse=''
        self.singleresposne=True
        say(prompt)
        self.assistant.start_conversation()
        while self.singledetectedresponse=='':
            time.sleep(.1)
        self.singleresposne=False
        return self.singledetectedresponse


    def custom_command(self,usrcmd):
        for i in range(1,numQuestion+1):
            try:
                for ques in custom_conversation['Conversation']['Question'][i]:
                    if str(ques).lower() in str(usrcmd).lower():
                        self.assistant.stop_conversation()
                        selectedans=random.sample(custom_conversation['Conversation']['Answer'][i],1)
                        say(*selectedans)
                        print("offline answer length = ", len(*selectedans))
                        # l = (int)(len(*selectedans))/8
                        # time.sleep(max(4,l))
                        break
            except Keyerror:
                say('Please check if the number of questions matches the number of answers')


        # for i in range(1,numInput+1):
        #     try:
        #         for ques in custom_conversation['Action']['Input'][i]:
        #             if str(ques).lower() in str(usrcmd).lower():
        #                 self.assistant.stop_conversation()
        #                 selectedans=random.sample(custom_conversation['Action']['Output'][i],1)
        #                 eval(selectedans[0])
        #                 break
        #     except Keyerror:
        #         say('Please check if the number of questions matches the number of answers')




    def main(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('--device-model-id', '--device_model_id', type=str,
                            metavar='DEVICE_MODEL_ID', required=False,
                            help='the device model ID registered with Google')
        parser.add_argument('--project-id', '--project_id', type=str,
                            metavar='PROJECT_ID', required=False,
                            help='the project ID used to register this device')
        parser.add_argument('--nickname', type=str,
                        metavar='NICKNAME', required=False,
                        help='the nickname used to register this device')
        parser.add_argument('--device-config', type=str,
                            metavar='DEVICE_CONFIG_FILE',
                            default=os.path.join(
                                os.path.expanduser('~/.config'),
                                'googlesamples-assistant',
                                'device_config_library.json'
                            ),
                            help='path to store and read device configuration')
        parser.add_argument('--credentials', type=existing_file,
                            metavar='OAUTH2_CREDENTIALS_FILE',
                            default=os.path.join(
                                os.path.expanduser('~/.config'),
                                'google-oauthlib-tool',
                                'credentials.json'
                            ),
                            help='path to store and read OAuth2 credentials')
        parser.add_argument('--query', type=str,
                        metavar='QUERY',
                        help='query to send as soon as the Assistant starts')
        parser.add_argument('-v', '--version', action='version',
                            version='%(prog)s ' + Assistant.__version_str__())

        args = parser.parse_args()
        with open(args.credentials, 'r') as f:
            credentials = google.oauth2.credentials.Credentials(token=None,
                                                                **json.load(f))

        device_model_id = None
        last_device_id = None
        try:
            with open(args.device_config) as f:
                device_config = json.load(f)
                device_model_id = device_config['model_id']
                last_device_id = device_config.get('last_device_id', None)
        except FileNotFoundError:
            pass

        if not args.device_model_id and not device_model_id:
            raise Exception('Missing --device-model-id option')

        should_register = (
            args.device_model_id and args.device_model_id != device_model_id)

        device_model_id = args.device_model_id or device_model_id
        with Assistant(credentials, device_model_id) as assistant:
            self.assistant = assistant
            
            subprocess.Popen(["aplay", "/home/pi/Robot-Niko/audio-files/welcome.wav".format(ROOT_PATH)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            events = assistant.start()
            device_id = assistant.device_id
            print('device_model_id:', device_model_id)
            print('device_id:', device_id + '\n')

            if should_register or (device_id != last_device_id):
                if args.project_id:
                    register_device(args.project_id, credentials,
                                    device_model_id, device_id, args.nickname)
                    pathlib.Path(os.path.dirname(args.device_config)).mkdir(
                        exist_ok=True)
                    with open(args.device_config, 'w') as f:
                        json.dump({
                            'last_device_id': device_id,
                            'model_id': device_model_id,
                        }, f)
                else:
                    print(WARNING_NOT_REGISTERED)

            for event in events:
                if event.type == EventType.ON_RENDER_RESPONSE:
                    #  mouthExpression("online", (int)(len(event.args["text"])) )
                    nothing = None
                if event.type == EventType.ON_START_FINISHED and args.query:
                    assistant.send_text_query(args.query)
                self.process_event(event)

        self.detector.terminate()


if __name__ == '__main__':
    try:
        Myassistant().main()
    except Exception as error:
        logging.exception(error)






