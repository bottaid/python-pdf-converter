import textract
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from io import StringIO
import re
# Open a PDF file.
fp = open('docs/matrice.pdf', 'rb')
f1 = open('docs/matrice.txt', 'w')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
print("Parser: ", parser)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser)
print ("Document: ", document)
retstr = StringIO()
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
laparams = LAParams()
codec = 'utf-8'
device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)

text = retstr.getvalue()
dict = {}
i = 0
for line in text:
    if line == "/n" or line == " ":
        i += 1
        continue
    else:
        dict[i] = line
        i += 1

print (dict)


#print (text)
f1.write(text)
fp.close()
f1.close()


'''
parser = PDFParser(f)
document = PDFDocument(parser)

outlines = document.get_outlines()
for (level, title, dest, a, se) in outlines:
    print (level, title)


f2 = open('docs/matrice.txt', 'r')
elenco = {}
Testo = f2.readlines()
for line in Testo:
    if line == "/n" or line == " ":
        continue
    if line != "/n":
        print (line)

f2.close()


elenco = {}
elenco['Nome'] = 'Dario'
elenco['Cognome'] = 'Bottai'
print (elenco.keys())
print (elenco.values())
print (elenco)

Matrice = {(0, 3): 1, (2, 1): 5, (3, 2): 7}
print (Matrice)
print (Matrice.keys())
print (Matrice.get((0, 2), 0))
print (Matrice.get((2, 1), 0))




a = np.arange(12)
print (a)
a = np.arange(12).reshape(2, 6)
print(a)
a[0] = 'Dario'
print (a)
'''


