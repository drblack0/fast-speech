from TTS.api import TTS
import torch 
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="This seems like a really fun project to do, I'm halfway through it already.",
                file_path="output.wav",
                speaker_wav="C:\\Users\\Kartik Saxena\\Downloads\\Music\\WhatsApp-Audio-2024-07-23-at-09.53.44_3544114e.waptt.wav",
                language="hi")

print(torch.cuda.is_available())