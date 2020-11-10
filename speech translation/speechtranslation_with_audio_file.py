import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import googletrans
import requests
response = requests.get("https://translate.google.com/")
english_voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
japan_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0"



r= sr.Recognizer()
with sr.AudioFile("motivational_speech.wav") as source:
    
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print(text)
       
        #convert text to target language
        translator = Translator()
        result= translator.translate(str(text), dest='ja')
        print("\n translate language")
        print(result.text)
        audio_text=result.text
        
        #convert text to audio
        engine = pyttsx3.init()
        engine.setProperty('voice', japan_voice_id)
        engine.say(str(audio_text))
        engine.runAndWait()
        
        
    except:
        print("sorry try again")

