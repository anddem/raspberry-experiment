from flask import Flask
from flask_restful import Api, Resource
import requests
# from telegram_bot import get_bot
import telebot
import telebot.types as tt
import os

def get_bot(token=None):
    token = os.environ.get('TELEGRAM_TOKEN') if token is None else token
    bot = telebot.TeleBot(token=token)

    @bot.message_handler(commands=['hello'])
    def send_hello(message: tt.Message):
        bot.reply_to(message, f'hello, {message.from_user.full_name}')

    @bot.message_handler(commands=['kill'])
    def kill_bot(message: tt.Message):
        bot.reply_to(message, 'killed')
        bot.stop_polling()
    
    @bot.message_handler(commands=['full'])
    def full_bot(message: tt.Message):
        bot.reply_to(message, message)

    return bot

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
bot = get_bot()

class Placeholder(Resource):
    def get(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1').json()
        return response

class SayHello(Resource):
    def get(self):
        
        bot.send_message(chat_id=335645770, text='Кто-то зашёл на сайт!')
        return 'sent'

api.add_resource(Placeholder, '/placeholder')
api.add_resource(SayHello, '/hello')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')