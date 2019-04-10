import logging
import urllib.request


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

url = "https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg_text}"
class bot():

    def __init__(self, bot_key, chat_id):
        self.bot_key = bot_key
        self.chat_id = chat_id

    def send(self, text):
        final_url = url.format(bot_key=self.bot_key, chat_id = self.chat_id, msg_text = text)
        response = urllib.request.urlopen(final_url)
        logging.info("Result: {}".format(response.read()))
