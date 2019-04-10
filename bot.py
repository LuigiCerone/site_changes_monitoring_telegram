import logging
import urllib2


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

url = "https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={channel_name}}&text={msg_text}}"
class bot():

    def __init__(self, bot_key, channel_name):
        self.bot_key = bot_key
        self.channel_name = channel_name

    def send(self, text):
        final_url = url.format(bot_key=self.bot_key, channel_name = self.channel_name, msg_text = text)
        response = urllib2.urlopen(final_url)
        loggin.info("Result: {}".format(response.read()))
