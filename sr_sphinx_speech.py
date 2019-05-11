import speech_recognition as sr

r = sr.Recognizer()

speech = sr.Microphone(device_index=0)

with speech as source:
    print("say something!...")
    audio = r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try: 
    recog = r.recognize_sphinx(audio)
    print("Sphinx thinks you said '" + recog + "'")  
except sr.UnknownValueError:  
    print("Sphinx could not understand audio")  
except sr.RequestError as e:  
    print("Sphinx error; {0}".format(e))
