import os
import requests

class Crawler:
        
    def getTrashPickUpDates(self, street) -> list:
        URL = f'https://wml2-abfallapp.regioit.de/abfall-app-wml2/rest/strassen/{street}/termine?fraktion=2&fraktion=3&fraktion=4&fraktion=5&fraktion=8&fraktion=10&fraktion=11'
        pickUpDates = requests.get(URL).json()
        print(pickUpDates)
        
        return pickUpDates

    def getFractionDetails (self) -> list:
        URL = 'https://wml2-abfallapp.regioit.de/abfall-app-wml2/rest/fraktionen'
        fractions = requests.get(URL).json()
        print(fractions)
        
        return fractions
