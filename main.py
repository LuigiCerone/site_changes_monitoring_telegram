from monitor import monitor
from bot import bot
import json

# https://api.telegram.org/bot<Token>/getUpdates

def main():
    data = load_json()
    url = data.get("url")
    telegram_bot = bot(data.get("bot_key"), data.get("chat_id"))
    
    try:
        # Read previous hash.
        with open("prev_hash.txt", "r+") as file:  
            prev_hash = file.read() 
        
            my_monitor = monitor(url, telegram_bot)    
            curr_hash = my_monitor.get_hash()
            if prev_hash != curr_hash:
                my_monitor.send_message("File changed")
            
            file.seek(0)
            file.write(curr_hash)
            
            file.close()
    except FileNotFoundError:
        open('prev_hash.txt', 'x').close()
        print("Previous hash not found.")

def load_json():
    data = None
    try:
        with open("conf.json") as file_json:
            data = json.load(file_json)
            
    except FileNotFoundError:
        open('conf.json', 'x').close()
        print("Add info to the configuration json file.")
    return data

if __name__=="__main__":
    main()