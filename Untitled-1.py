# TELEGRAM_BOT_TOKEN = '6384605708:AAEzqbyJnXu0yAdNFZvUBaK8fcpTEvseuNo'
# TELEGRAM_CHAT_ID = '71046013'
from flask import Flask, render_template, request
import telepot

app = Flask(__name__)
app.debug = True

TELEGRAM_BOT_TOKEN = '6384605708:AAEzqbyJnXu0yAdNFZvUBaK8fcpTEvseuNo'
TELEGRAM_CHAT_ID = '71046013'

@app.route('/')
def home():
    return render_template('report.html')

@app.route('/submit', methods=['POST'])
def submit():
    reporter = request.form['reporter']
    location = request.form['location']
    complaint = request.form['complaint']

    message = f'신고자: {reporter}\n위치: {location}\n불편내용: {complaint}'

    send_telegram_message(message)

    return '신고가 접수되었습니다. 감사합니다!'

def send_telegram_message(message):
    bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
    bot.sendMessage(TELEGRAM_CHAT_ID, message)

if __name__ == '__main__':
    app.run()
