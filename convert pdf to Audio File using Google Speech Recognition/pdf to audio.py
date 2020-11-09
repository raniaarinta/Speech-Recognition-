import pyttsx3
import PyPDF2 as pdf
from gtts import gTTS
import os
import requests
response = requests.get("https://translate.google.com/")
#read pdf file
pdf_file=open("Rania's Paper.pdf","rb")
pdf_reader= pdf.PdfFileReader(pdf_file)
pages=pdf_reader.numPages
page=pdf_reader.getPage(1)
text_pdf=page.extractText()
#convert text to audio

engine = pyttsx3.init()
engine.say(text_pdf)
engine.runAndWait()
#save audio file

ttmp3 =  gTTS(text=text_pdf,lang="en",tld="com")
ttmp3.save("pdf_to_audio.mp3")
os.startfile("pdf_to_audio.mp3")