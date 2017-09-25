from model.esercizio import Esercizio
from model.power import Power
from model.rom import ROM
from model.sway import Sway

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
    oggettoEsercizioGenerico = Esercizio("Esercizio generico")
    oggettoEsercizioPower = Power("Esercizio power")
	oggettoEsercizioRom = ROM("Esercizio rom")
	oggettoEsercizioSway = Sway("Esercizio sway")


    oggettoEsercizioGenerico.stampaNome()
    oggettoEsercizioPower.stampaNome()
	oggettoEsercizioRom.stampaNome()
	oggettoEsercizioSway.stampaNome()

    print ("Hello world dal main")
    

if __name__ == '__main__':
    main()
