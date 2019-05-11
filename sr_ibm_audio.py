import speech_recognition as sr
from ibm_watson import SpeechToTextV1
import json

r = sr.Recognizer()

speech_to_text = SpeechToTextV1(
    iam_apikey = "YOUR_KEY",
    url="YOUR_URL"
)


with open('FILE_NAME.wav', 'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav'
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))
   