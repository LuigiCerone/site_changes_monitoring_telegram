# site_changes_monitoring_telegram

This project is a very simple script that I've developed to monitor changes in a remote site and get notified with a Telegram messages when it is modified.

In order to use it:

+ Create a bot with the bot father and start it.
+ Get the chat_id by using [https://api.telegram.org/bot[*TOKEN*]/getUpdates](https://api.telegram.org/bot[TOKEN]/getUpdates) where TOKEN should be replaced with the one of your new bot.
+ Insert the information into conf.json file:
 For example:
 ``` javascript
 {
    "url": "http://example.com",
    "bot_key": "TOKEN",
    "chat_id": 00000000
} 
```
+ Create a cronjob with the main.py file and get notified.

The project's logic is based on previous hash vs new hash comparison, so this code works only with static websites.