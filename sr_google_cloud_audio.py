import speech_recognition as sr
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="SERVICE_ACCOUNT_KEY.json"

r = sr.Recognizer()
file = sr.AudioFile('FILE_NAME.wav')

with file as source:
    audio = r.record(source)

try:
    recog = r.recognize_google_cloud(audio, language = 'en-US')

    print("You said: " + recog)
except sr.UnknownValueError as u:
    print(u)
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 