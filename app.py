from flask import Flask, request
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

from chatterbot import ChatBot
from chatterbot.trainers import UbuntuCorpusTrainer

app = Flask(__name__, static_folder='build', static_url_path='')
CORS(app, resources={ r'/*': {'origins':'*'} })
app.config['CORS_HEADERS'] = 'Content-Type'

chatbot = ChatBot('ChatBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer = UbuntuCorpusTrainer(chatbot)
trainer.train()


@app.route('/')
@cross_origin()
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/chat', methods=['POST'])
@cross_origin()
def chat():
    message = str(chat_bot.get_response(request.json['message']))
    return {'message': message}
    
    
    
if __name__ == '__main__':
   app.run(debug=True)