import speech_recognition as sr

r = sr.Recognizer()

file = sr.AudioFile("FILE_NAME.wav")

with file as source:
    audio = r.record(source)

try:
    recog = r.recognize_wit(audio, key = "YOUR_KEY")
    print("You said: " + recog)
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("Could not request results ; {0}".format(e))


