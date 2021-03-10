import logging
from flask import Flask,request
from telegram import Bot, Update, ReplyKeyboardMarkup
from dialog import get_reply
from newsClient import fetch_news,topics
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, Dispatcher, dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger=logging.getLogger(__name__)
app=Flask(__name__)
TOKEN='1682075396:AAH_D55yihaezjdtZQ20ICFm2CTsX_0yd1s'
@app.route('/start')
def start():
    return 'Hello!'
@app.route(f'/{TOKEN}',methods=['GET','POST'])
def webhook():
    update=Update.de_json(request .get_json(),bot)
    dp.process_update(update)
    return 'ok'
def start(update,context):
    print(update)
    author=update.message.from_user.first_name
    repy="Hi! {}".format(author)
    context.bot.sendMessage(chat_id=update.message.chat_id,text=repy)
def help(update,context):
    author = update.message.from_user.first_name
    title=update.message.from_user.last_name
    msg=f'Hey {author} {title} what help do you need?'
    context.bot.sendMessage(chat_id=update.message.chat_id,text=msg)
def error(update,context):
    logger.error('Your error is %s ',update)
def reply_text(update,context):
    intent,reply=get_reply(update.message.text,update.message.chat_id)
    if intent=='get_news':
        articles=fetch_news(reply)
        for article in articles:
            context.bot.sendMessage(chat_id=update.message.chat_id,text=article['link'])
    else:
        context.bot.sendMessage(chat_id=update.message.chat_id,text=reply)

def echo_sticker(update,context):
    context.bot.sendSticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)
def news(update,context):
    context.bot.sendMessage(chat_id=update.message.chat_id,text="Choose a news category",
                            reply_markup=ReplyKeyboardMarkup(keyboard=topics,one_time_keyboard=True))



if __name__ == '__main__':
    bot = Bot('1682075396:AAH_D55yihaezjdtZQ20ICFm2CTsX_0yd1s')
    # instance=Updater('1682075396:AAH_D55yihaezjdtZQ20ICFm2CTsX_0yd1s')
    bot.set_webhook('https://665d65c57d27.ngrok.io/' + TOKEN)
    dp = Dispatcher(bot,None)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('news',news))
    dp.add_handler(MessageHandler(Filters.text, reply_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)
    app.run(port=8443)
