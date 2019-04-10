import hashlib
import urllib.request

class monitor():

    def __init__(self, url, bot):
        self.url = url
        self.telegram_bot = bot

    def get_hash(self):        
        response = urllib.request.urlopen(self.url)
        content = response.read()
        return hashlib.sha224(content).hexdigest()

    def send_message(self, msg_txt="Changed!"):
        self.telegram_bot.send(msg_txt) 
