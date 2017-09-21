from src.model.esercizio import Esercizio
from src.model.power import Power


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
    
    oggettoEsercizioGenerico.stampaNome()
    oggettoEsercizioPower.stampaNome()

    print ("Hello world dal main")
    

if __name__ == '__main__':
    main()
