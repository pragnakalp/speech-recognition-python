import speech_recognition as sr

r = sr.Recognizer()

file = sr.AudioFile('FILE_NAME.wav')

with file as source:
    audio = r.record(source)

# Audio Transcription using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    recog = r.recognize_google(audio, language = 'en-GB')
    print("You said: " + recog)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))