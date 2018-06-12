from flask import Flask
from flask import request
import telegram
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'aYT>.L$kk2h>!'

CHAT_ID = 'chatID'
TOKEN = 'botToken'

bot = telegram.Bot(token=TOKEN)

@app.route('/alert', methods = ['POST'])
def postAlertmanager():

    content = request.get_json()

    try:

        for alert in content['alerts']:

            message = """
Status """+alert['status']+"""
    
Alertname: """+alert['labels']['alertname']+"""

Instance: """+alert['labels']['instance']+"""("""+alert['labels']['name']+""")
    
"""+alert['annotations']['description']+"""
"""
            bot.sendMessage(chat_id=CHAT_ID, text=message)
    except Exception as e:

        logger.info(content)
        bot.sendMessage(chat_id=CHAT_ID, text=e)

    return

if __name__ == '__main__':
    logging.basicConfig(filename='flaskAlert.log',level=logging.INFO)
    app.run(host='0.0.0.0', port=9119)
