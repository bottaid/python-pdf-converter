from PyPDF2 import PdfFileReader


class Esercizio(object):

    def __init__(self, nome, pdfFileObject):
        self.nome = nome
        self.pdfReader = PdfFileReader(pdfFileObject)

    def stampaNome(self):
        print (self.nome)

    def stampaPagine(self):
        pageObject = self.pdfReader.getPage(0).extractText() + "\n"
        print("Contenuto: ", pageObject)
