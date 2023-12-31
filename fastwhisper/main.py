

import time

from faster_whisper import WhisperModel

model_size = "large-v2"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", compute_type="float16")


start = time.perf_counter()
segments, info = model.transcribe("../output.wav", beam_size=5)
end = time.perf_counter()


for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

print('recognized time ======================: ', end - start)
