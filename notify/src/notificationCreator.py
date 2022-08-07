import datetime
import fractions
from dateutil import parser
import requests
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from fractionMapper import FractionMapper

class NotificationCreator:
    
    def __init__(self) -> None:
        self.fractionMapper = FractionMapper()
        self.client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

    def createNotification(self, entry) -> None:
        
        pickupDate = parser.parse(entry["datum"])
        
        if(pickupDate < datetime.datetime.now()):
            return
        
        previousDay = pickupDate - datetime.timedelta(days=1)
        scheduled_time = datetime.time(hour=19, minute=30)
        schedule_timestamp = datetime.datetime.combine(previousDay, scheduled_time).strftime('%s')
        fraction = self.fractionMapper.getFraction(entry["bezirk"]["fraktionId"])

        # Channel you want to post message to
        channel_id = os.getenv("CHANNEL_ID")
        
        #Build the message
        attachmentsStr = '[{"color": "TRASH_TYPE_COLOR","fields": [{"title": "Welche?","value": "TRASH_TYPE_VALUE","short": true},{"title": "Wann?","value": "TRASH_PICKUP_DATE","short": true }]}]'
        attachmentsStr = attachmentsStr.replace("TRASH_TYPE_COLOR", f'#{fraction[f"farbeRgb"]}')
        attachmentsStr = attachmentsStr.replace("TRASH_TYPE_VALUE", fraction["name"])
        attachmentsStr = attachmentsStr.replace("TRASH_PICKUP_DATE", entry["datum"])

        try:
            # Call the chat.scheduleMessage method using the WebClient
            result = self.client.chat_scheduleMessage(
                text="Mülltonne rausstellen!",
                channel=channel_id,
                blocks='[{"type": "header","text": {"type": "plain_text","text": "Mülltonne rausstellen!","emoji": true}}]',
                attachments=attachmentsStr,
                post_at=schedule_timestamp
            )
            
            print(result)

        except SlackApiError as e:
            print("Error scheduling message: {}".format(e))

    
