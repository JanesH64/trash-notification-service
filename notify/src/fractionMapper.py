import os
import string
from mongo import DatabaseConnector

class FractionMapper:

    def __init__(self) -> None:
        databaseConnector = DatabaseConnector()
        self.fractions = databaseConnector.get_fractions()
        
    def getFraction(self, fractionId) -> string:
        return self.fractions[fractionId]
    
