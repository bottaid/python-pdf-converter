import PyPDF2
import textract as textract
from PyPDF2 import PdfFileReader

import pdfminer

from pdfminer.pdfinterp import PDFResourceManager, process_pdf, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
import io

class Esercizio(object):

    def __init__(self, nome, pdfFileObject):
        self.nome = nome
        self.pdfReader = PdfFileReader(pdfFileObject)

    def stampaNome(self):
        print (self.nome)

    def stampaPagine(self):
         pageObject = self.pdfReader.getPage(i).extractText() + "\n"
         print("Contenuto: ", pageObject)

    def convert_pdf(path):

        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

        fp = open(path, 'rb')
        process_pdf(rsrcmgr, device, fp)
        fp.close()
        device.close()

        str = retstr.getvalue()
        print (str)
        retstr.close()
        return str

    def convert_pdf_to_txt(path):
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                      password=password,
                                      caching=caching,
                                      check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()
        return text

    def convertpdftotext(path):
        fp = open(path, 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize('')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        laparams.char_margin = 1.0
        laparams.word_margin = 1.0
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        extracted_text = ''

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    extracted_text += lt_obj.get_text()
