import logging
from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,CallbackContext

logging.basicConfig(format='%(asctime)s -%(name)s - %(levelname)s - %(message)s' , level=logging.INFO)
logger=logging.getLogger(__name__)
TOKEN='1684452519:AAG4lw4IlPkmatUvSIf00xegX-34xxhy1Uk'

def start(bot,update):
    print(update)
    author = update.message.from_user.first_name
    reply = "Hi! {} there".format(author)
    bot.reply_text(chat_id=update.message.chat_id,text=reply)
def _help(bot,update):
    #author = update.message.from_user.first_name
    reply_help = "Hi! cocksucker you want help!"
    bot. send_message(chat_id=update.message.chat_id, text=reply_help)
def echo_text(bot,update):
    reply=update.message.text
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def echo_sticker(bot,update):
    bot.send_sticker(bot.send_message(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id))
def  error(bot, update):
    logger.error(f"U got some message {update, update.error}")
def main():

    updater=Updater(TOKEN)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("start",_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)
    updater.start_polling()
    logger.info("The bot is live")
    updater.idle()

if __name__ == '__main__':
    main()
