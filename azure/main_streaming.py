

import os
import time
import threading
from scipy.io import wavfile

import azure.cognitiveservices.speech as speechsdk


channels = 1
bits_per_sample = 16
samples_per_second = 16000

# Create audio configuration using the push stream
wave_format = speechsdk.audio.AudioStreamFormat(
    samples_per_second, bits_per_sample, channels)

stream = speechsdk.audio.PushAudioInputStream(stream_format=wave_format)
audio_config = speechsdk.audio.AudioConfig(stream=stream)


speech_config = speechsdk.SpeechConfig(subscription=os.environ.get(
    'SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

speech_config.speech_recognition_language = "zh-CN"

# instantiate the speech recognizer with push stream input
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, audio_config=audio_config)
recognition_done = threading.Event()

# Connect callbacks to the events fired by the speech recognizer

first = True


start = None
end = None


def session_stopped_cb(evt):
    """callback that signals to stop continuous recognition upon receiving an event `evt`"""
    print('SESSION STOPPED: {}'.format(evt))
    recognition_done.set()


def recognized_cb(evt):
    """callback that signals to stop continuous recognition upon receiving an event `evt`"""
    print('RECOGNIZED: {}'.format(evt))
    global first
    global start
    global end
    if first:
        first = False
        end = time.perf_counter()
        print('recognized time ======================: ', end - start)


speech_recognizer.recognized.connect(recognized_cb)
speech_recognizer.session_started.connect(
    lambda evt: print('SESSION STARTED: {}'.format(evt)))

# start continuous speech recognition
speech_recognizer.start_continuous_recognition()


start = time.perf_counter()

_, wav_data = wavfile.read('../output.wav')
stream.write(wav_data.tobytes())
stream.close()


while not recognition_done.wait(timeout=1.0):
    pass
