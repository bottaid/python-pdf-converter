import os

from src.model.esercizio import Esercizio
from src.model.power import Power
from src.model.rom import Rom
from src.model.sway import Sway


def main():
    '''
    controllaArgomenti()
    controllaEstensioneFile()
    controllaDimensioneTabella()
    estrazioneDocumento()
    estrazioneTabella()
    controllaCsvEsistente()
    creaNuovoCsv()
    '''
    path = 'docs'

    directory = os.fsencode(path)

    for file in os.listdir(directory):
        #documentoMappa
        filename = os.fsdecode(file)
        with open(os.path.join(directory, file), 'rb') as pdfFileObject:
            if (filename.startswith("sway_") & filename.endswith(".pdf")):
                print ("File pronto per conversione: " + filename)
                pdf = Sway(filename, path)
                pdf.stampaPagine()
            elif (filename.startswith("rom_") & filename.endswith(".pdf")):
                print ("File pronto per conversione: " + filename)
                pdf = Rom(filename, path)
            elif (filename.startswith("power_") & filename.endswith(".pdf")):
                print ("File pronto per conversione: " + filename)
                pdf = Power(filename, path)
            else:
                print ("File non convertibile: " + filename)

            if (isinstance(pdf, Esercizio)):
                print("***Processando: ")
                pdf.stampaNome()


    print ("Hello world dal main")
    

if __name__ == '__main__':
    main()
