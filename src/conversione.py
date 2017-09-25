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
    path = '/docs'

    oggettoEsercizioGenerico = Esercizio("Esercizio generico")
    oggettoEsercizioPower = Power("Esercizio power")
    oggettoEsercizioRom = Rom("Esercizio rom")
    oggettoEsercizioSwayDue = Sway("Esercizio sway")


    oggettoEsercizioGenerico.stampaNome()
    oggettoEsercizioPower.stampaNome()
    oggettoEsercizioRom.stampaNome()
    oggettoEsercizioSwayDue.stampaNome()

    print ("Hello world dal main")
    

if __name__ == '__main__':
    main()
