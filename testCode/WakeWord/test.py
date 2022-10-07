import os
from eff_word_net.streams import SimpleMicStream
from eff_word_net.engine import HotwordDetector
from eff_word_net import samples_loc

mycroft_hw = HotwordDetector(
        hotword="vision",
        reference_file = os.path.join(samples_loc,"vision_ref.json"),
        threshold=0.7,
        relaxation_time = 0.8 
    )

mic_stream = SimpleMicStream()
mic_stream.start_stream()

print("Say vision")
while True :
    frame = mic_stream.getFrame()
    result = mycroft_hw.scoreFrame(frame)
    if result==None :
        print("No voice..")
        continue
    if(result["match"]):
        print("Wakeword uttered",result["confidence"])
