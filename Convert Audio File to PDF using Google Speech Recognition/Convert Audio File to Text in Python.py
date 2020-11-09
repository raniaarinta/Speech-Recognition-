import speech_recognition as sr
from fpdf import FPDF 
r= sr.Recognizer()
with sr.AudioFile("motivational_speech.wav") as source:
    
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print(text)
    except:
        print("sorry try again")
#convert text to pdf file
pdf=FPDF()
pdf.add_page()
pdf.set_font('Courier','B',16)
pdf.cell(40,10,text)
pdf.output('result.pdf','F')
#onvert text to txt file
file1 = open("output_audio.txt","w")
file1.writelines(text) 
file1.close() 