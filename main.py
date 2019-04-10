import monitor
import bot

def main():
    url = ""
    telegram_bot = bot()
    
    # Read previous hash.
    with open("prev_hash.txt") as file:  
        prev_hash = file.read() 
    
        my_monitor = monitor(url)    
        curr_hash = my_monitor.get_hash()
        if prev_hash != curr_hash:
            my_monitor.send_message("File changed")
        
        file.close()

if __name__=="__main__":
    main()