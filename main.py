# Загрузчик видео с YouTube (в видео и аудио версиях)
from controller import * 
import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = '5630119738:AAE1fSRlZKFqHRTflJMsjcXUG9mvtbA6bgw'
bot = telegram.Bot(token=TOKEN)
print(bot.get_me())

updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('hi', start))
updater.dispatcher.add_handler(CommandHandler('res', get_resolution))
updater.dispatcher.add_handler(CommandHandler('bit', get_bitrate))
updater.dispatcher.add_handler(CommandHandler('video', get_video))
updater.dispatcher.add_handler(CommandHandler('audio', get_audio))
updater.dispatcher.add_handler(CommandHandler('help', help))

print('server start')
updater.start_polling()
updater.idle()