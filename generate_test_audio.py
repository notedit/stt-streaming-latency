

from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "test.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="今天是 2024 年 1月 1 日，新的一年开始了。请问有什么我可以帮助你的嘛"
)

response.stream_to_file(speech_file_path)
