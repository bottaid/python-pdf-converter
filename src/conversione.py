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
        filename = os.fsdecode(file)
        if (filename.startswith("sway_") & filename.endswith(".pdf")):
            print ("File pronto per conversione: " + filename)
            file = Sway(filename)
        elif (filename.startswith("rom_") & filename.endswith(".pdf")):
            print ("File pronto per conversione: " + filename)
            file = Rom(filename)
        elif (filename.startswith("power_") & filename.endswith(".pdf")):
            print ("File pronto per conversione: " + filename)
            file = Power(filename)
        else:
            print ("File non convertibile: " + filename)

        if (isinstance(file, Esercizio)):
            print("***Processando: ")
            file.stampaNome()


    print ("Hello world dal main")
    

if __name__ == '__main__':
    main()
