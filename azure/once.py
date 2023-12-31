

import os
import time
import azure.cognitiveservices.speech as speechsdk


def from_file():

    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get(
        'SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

    speech_config.speech_recognition_language = "zh-CN"

    audio_config = speechsdk.AudioConfig(filename="../output.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config)

    start = time.perf_counter()
    result = speech_recognizer.recognize_once_async().get()

    end = time.perf_counter()
    print(result.text)
    print('recognized time ======================: ', end - start)


from_file()
