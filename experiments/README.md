# Experiments

The first tests from 2022, made before the main program in [`src/`](../src)
came together. They are kept as they were, as a record of how Niko's voice and
movement were worked out.

| Folder | What it tried |
|---|---|
| [`listen/`](listen) | Speech recognition three ways: Google's web page in Chrome through Selenium (`Listen1.py`), the SpeechRecognition library (`Listen2.py`), and Vosk, offline (`Listen3.py`) |
| [`speak/`](speak) | Text to speech: web voices through Selenium (ttsmp3.com, naturalreaders.com, text-to-speech.org and ttsreader.com, in `Speak1.py`, `Speak2.py` and `talk3.py` to `talk5.py`), pyttsx3 (`Speak3.py`, `talk-test.py`) and Google Translate's voice (`speech.sh`) |
| [`servo/`](servo) | Servos on a PCA9685 board: a sweep, the jaw and the neck |
| [`motor/`](motor) | Driving the two wheel motors from the keyboard |

The Selenium tests use `/usr/bin/chromedriver`, from Raspberry Pi OS's
`chromium-chromedriver` package. `Listen3.py` loads its model from
`listen/DataBase/`: download `vosk-model-small-en-us-0.15` from
[alphacephei.com/vosk/models](https://alphacephei.com/vosk/models) and unzip
it there.
