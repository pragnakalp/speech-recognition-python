import speech_recognition as sr

r = sr.Recognizer()

file = sr.AudioFile('FILE_NAME.wav')

#for audio transcription    
with file as source:
    audio = r.record(source)

# recognize speech using Sphinx  
try:  
    recog = r.recognize_sphinx(audio)
    print("Sphinx thinks you said '" + recog + "'")  
except sr.UnknownValueError:  
    print("Sphinx could not understand audio")  
except sr.RequestError as e:  
    print("Sphinx error; {0}".format(e))
