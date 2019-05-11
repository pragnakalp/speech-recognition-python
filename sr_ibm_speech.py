import speech_recognition as sr
from ibm_watson import SpeechToTextV1
import json

r = sr.Recognizer()
speech = sr.Microphone()


speech_to_text = SpeechToTextV1(
    iam_apikey = "YOUR_API_KEY",
    url="YOUR_URL"
)

print('speech_to_text: '+str(speech_to_text))

with speech as source:
    print("say something!!...")
    audio_file = r.adjust_for_ambient_noise(source)
    audio_file = r.listen(source)
print('audio_file: '+str(audio_file))

speech_recognition_results = speech_to_text.recognize(audio=audio_file.get_wav_data(), content_type='audio/wav').get_result()
print(json.dumps(speech_recognition_results, indent=2))
