from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello! welcome to P&P Store.')

def help(update, context):
    update.message.reply_text('How can I assist you?')

def main():
    updater = Updater("7329473272:AAGn0_p9RWpLMjQWlTuhUvP8I1DhK0lIvYs", use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
