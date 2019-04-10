import hashlib
import urllib2

class monitor():

    def __init__(self, url, bot):
        self.url = url
        self.telegram_bot = bot

    def get_hash(self):        
        response = urllib2.urlopen(self.url)
        content = response.read()
        return hashlib.sha224(content).hexdigest()

    def send_message(self, msg_txt="Changed!"):
        self.telegram_bot.send(msg_txt) 
