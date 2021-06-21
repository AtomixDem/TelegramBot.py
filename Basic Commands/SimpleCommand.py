import sys
import time
import telepot # Default Library for Telegram Bot


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)


    # Start command
    if command == '/start': # Your command
        bot.sendMessage(chat_id, "This is my start command! Write here my commands or a description.") # Bot message
    
    # Commands or messages
    if command == 'Hello': #Your message
        bot.sendMessage("Hi, I am a Telegram Bot!") # Bot message
        


bot = telepot.Bot('PASTE YOUR TOKEN HERE') # Paste your Token Bot here
bot.message_loop(handle)
print('The bot is ONLINE!') # When the bot is online, print this in the console
