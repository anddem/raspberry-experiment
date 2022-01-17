from flask import Flask, make_response, render_template, send_file
from flask_restful import Api, Resource
import telebot
import telebot.types as tt
import os
import cv2


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


class CameraImage(Resource):
    def get(self):
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            return make_response({'message': "can't open camera stream"}, 500)
        try:
            ret, frame = camera.read()
            image_path = os.path.join(os.curdir, 'images', 'response.png')
            cv2.imwrite(image_path, frame)
            template = render_template('template.html')
            return make_response(template)
        finally:
            camera.release()


class GetImage(Resource):
    def get(self, image: str):
        file = os.path.join(os.curdir, 'images', image)
        return send_file(file)


api.add_resource(CameraImage, '/camera')
api.add_resource(GetImage, '/images/<image>')


class GetImage(Resource):
    def get(self, image: str):
        file = os.path.join(os.curdir, 'images', image)
        return send_file(file)



api.add_resource(GetImage, '/images/<image>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')