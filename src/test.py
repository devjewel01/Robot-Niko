import os
import os.path
import yaml
import random

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))

with open('{}/src/test.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    test = yaml.load(conf, Loader=yaml.FullLoader)


numQuestion = len(test['Conversation']['Question'])
numAnswer = len(test['Conversation']['Answer'])

def check(usrcmd):
    for i in range(1,numQuestion+1):
        for ques in (test['Conversation']['Question'][i]):
            if str(ques).lower() in str(usrcmd).lower():
                selectedAns=random.sample(test['Conversation']['Answer'][i],1)
                print(*selectedAns)
                
                break
            