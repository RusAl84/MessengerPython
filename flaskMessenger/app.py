import json
import time
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)
ListOfMessages = []

@app.route('/')
def dafault_route():
    return 'Messenger Flask server is running! ' \
           '<br> <a href="/status">Check status</a>'

@app.route('/status')
def status():
    return {
        'messages_count': len(ListOfMessages)
    }

# отправка сообщений
@app.route("/api/Messanger", methods=['POST'])
def SendMessage():
    msg = request.json
    print(msg)
    # messages.append({ "UserName":"RusAl","MessageText":"Privet na sto let!!!","TimeStamp":"2021-03-05T18:23:10.932973Z"})
    ListOfMessages.append(msg)
    print(msg)
    msgtext = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Всего сообщений: {len(ListOfMessages)} Посланное сообщение: {msgtext}")
    return f"Сообщение отослано успшно. Всего сообщений: {len(ListOfMessages)} ", 200


# получение сообщений
@app.route("/api/Messanger/<int:id>")
def GetMessage(id):
    print(id)
    if id >= 0 and id < len(ListOfMessages):
        print(ListOfMessages[id])
        return ListOfMessages[id], 200
    else:
        return "Not found", 400

if __name__ == '__main__':
    app.run()
