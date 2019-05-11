import speech_recognition as sr

r = sr.Recognizer()

speech = sr.Microphone()

with speech as source:
    print("say something!!....")
    audio = r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    recog = r.recognize_wit(audio, key = "YOUR_KEY")
    print("You said: " + recog)
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("Could not request results ; {0}".format(e))


