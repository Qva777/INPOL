import requests
import telebot as telebot
from env_config import BOT_ID

bot = telebot.TeleBot(BOT_ID)


def send_photo(chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo)


# get user ID From Telegram
# bot_token = BOT_ID
# response = requests.get(f'https://api.telegram.org/bot{bot_token}/getUpdates')
# chat_id = response.json()['result'][0]['message']['chat']['id']
# print(f'Your chat ID is: {chat_id}')
