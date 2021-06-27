# flask , django 做伺服器的主流套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('CAPxMsvvYAI07W8Lc32TshDLApWjKHlrXJMlJttomQOGfiJyBWugrNdG8Pnzqq5pVZuc85c0CUzS0KNRlqTN9uH/M94PquFuD9m0vwXJ0Rkmir8A0FqIcHrgoNCg61YDZ+GFdk0QAy7+WkxVDpI3igdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('63ca7ae3e25345ef83d28ed30530bbad')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉，我看不懂你說什麼'

    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()