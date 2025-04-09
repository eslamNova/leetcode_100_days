import whisper

model = whisper.load_model("small")

result = model.transcribe("L1.mp3", language="ar")

print(result["text"])