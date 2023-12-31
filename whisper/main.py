

import time
from openai import OpenAI
client = OpenAI()

audio_file = open("../output.wav", "rb")
start = time.perf_counter()
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)
end = time.perf_counter()
print(transcript)
print('recognized time ======================: ', end - start)
