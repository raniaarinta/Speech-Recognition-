import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
    print("try to speak")
    audio=r.listen(source)
    
    try:
        text=r.recognize_google(audio)
        print("you said: {}".format(text))
    except:
        print("sorry we can't regonize your voice")