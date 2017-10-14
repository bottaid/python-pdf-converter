from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfpage import PDFPage
from io import StringIO

class Esercizio(object):

    def __init__(self, filename, path):
        self.filename = filename
        self.path = path + '/'

        fp = open(self.path + self.filename, 'rb')
        # Create a PDF parser object associated with the file object.
        parser = PDFParser(fp)
        print("Parser: ", parser)
        # Create a PDF document object that stores the document structure.
        # Supply the password for initialization.
        self.document = PDFDocument(parser)
        print ("Document: ", self.document)
        self.retstr = StringIO()
        # Check if the document allows text extraction. If not, abort.
        if not self.document.is_extractable:
            raise PDFTextExtractionNotAllowed
        # Create a PDF resource manager object that stores shared resources.
        rsrcmgr = PDFResourceManager()
        # Create a PDF device object.
        laparams = LAParams()
        codec = 'utf-8'
        device = TextConverter(rsrcmgr, self.retstr, codec=codec, laparams=laparams)
        # Create a PDF interpreter object.
        self.interpreter = PDFPageInterpreter(rsrcmgr, device)
        device.close()

    def stampaNome(self):
        print (self.path + self.filename)

    def stampaPagine(self):
         for page in PDFPage.create_pages(self.document):
                self.interpreter.process_page(page)

         text = self.retstr.getvalue()
         print (text)
         self.retstr.close()


