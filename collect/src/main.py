from dotenv import load_dotenv, find_dotenv
from mongo import DatabaseConnector
import os
from crawler import Crawler;

load_dotenv(find_dotenv())

crawler = Crawler()
mongo = DatabaseConnector()

STREET = os.getenv('STREET')
pickupDates = crawler.getTrashPickUpDates(STREET)
fractions = crawler.getFractionDetails()

mongo.update_pickupDates(pickupDates)
mongo.update_fractions(fractions)





