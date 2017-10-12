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
# Open a PDF file.
fp = open('docs/sway_nomefile.pdf', 'rb')
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
print (text)




