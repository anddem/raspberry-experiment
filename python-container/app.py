from flask import Flask, send_file
from flask_restful import Api, Resource
import telebot
import telebot.types as tt
import os


def get_bot(token='1694530843:AAHycibEgQoqB0udvbUVn80jCcqUA-vnwnc'):
    token = os.environ.get('TELEGRAM_TOKEN') if token is None else token
    bot = telebot.TeleBot(token=token)

    @bot.message_handler(commands=['hello'])
    def send_hello(message: tt.Message):
        bot.reply_to(message, f'hello, {message.from_user.full_name}')

    return bot

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
bot = get_bot()


class GetImage(Resource):
    def get(self, image: str):
        file = os.path.join(os.curdir, 'images', image)
        return send_file(file)



api.add_resource(GetImage, '/images/<image>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')