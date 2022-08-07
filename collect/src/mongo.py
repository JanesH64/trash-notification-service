from pymongo import MongoClient
from datetime import datetime
import os

class DatabaseConnector:

    def __init__(self) -> None:
        self.db = MongoClient(os.getenv('MONGO_URI')).trashnotificationservice

    def update_pickupDates(self, entries: list) -> None:
        if(len(entries) > 0):
            self.db.pickupDates.delete_many({})
            self.db.pickupDates.insert_many(entries)
         
         
    def update_fractions(self, entries: list) -> None:
        if(len(entries) > 0):
            self.db.fractions.delete_many({})
            self.db.fractions.insert_many(entries)
    
