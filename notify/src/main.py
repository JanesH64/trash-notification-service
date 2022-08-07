from dotenv import load_dotenv, find_dotenv

from notificationCreator import NotificationCreator
from mongo import DatabaseConnector

import time



load_dotenv(find_dotenv())

notificationCreator = NotificationCreator()
databaseConnector = DatabaseConnector()

pickupDates = databaseConnector.get_pickupDates()

for entry in pickupDates:
    notificationCreator.createNotification(entry)
    time.sleep(1.00)
    




