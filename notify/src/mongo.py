from pymongo import MongoClient, cursor
from datetime import datetime
import os

class DatabaseConnector:

    def __init__(self) -> None:
        self.db = MongoClient(os.getenv('MONGO_URI')).trashnotificationservice

    def get_pickupDates(self) -> list:
            return self.db.pickupDates.find({})
         
         
    def get_fractions(self) -> list:
            return self.db.fractions.find({})
    
