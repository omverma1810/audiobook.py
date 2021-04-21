import pyttsx3
import PyPDF2

book = open('your selected.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
recon = pyttsx3.init()
for num in range(from which page you want it to read in integers, pages):
    page = pdfReader.getPage(page number in integers)
    text = page.extractText()
    recon.say(text)
    recon.runAndWait()
