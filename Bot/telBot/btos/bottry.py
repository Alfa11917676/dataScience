import logging
from flask import Flask,request
from telegram import Bot, Update
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
    update=Update.de_json(request.get_json(),bot)
    dp.process_update(update)
    return 'ok'
def start(update,context):
    print(update)
    author=update.message.from_user.first_name
    repy="Hi! {}".format(author)
    context.bot.sendMessage(chat_id=update.message.chat_id,text=repy)
def _help(update,context):
    author = update.message.from_user.first_name
    title=update.message.from_user.last_name
    msg=f'Hey {author} {title} what help do you need?'
    context.bot.sendMessage(chat_id=update.message.chat_id,text=msg)
def error(update,context):
    logger.error('Your error is %s is caused by %s',update,update.error)
def echo_text(update,context):
    reply=update.message.text
    context.bot.sendMessage(chat_id=update.message.chat_id,text=reply)
def echo_sticker(update,context):
    context.bot.sendSticker   (chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)


if __name__ == '__main__':
    bot = Bot('1682075396:AAH_D55yihaezjdtZQ20ICFm2CTsX_0yd1s')
    # instance=Updater('1682075396:AAH_D55yihaezjdtZQ20ICFm2CTsX_0yd1s')
    bot.set_webhook('https://76530a23aea3.ngrok.io/' + TOKEN)
    dp = Dispatcher(bot, None)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('_help', _help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)
    app.run(port=8443)