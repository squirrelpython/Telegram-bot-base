from bot_base import *

def start(update: Update, context: CallbackContext):
    message = update.message
    user = message.from_user
    message.reply_text(f'Hello *{user.first_name}*')
    return


CONFIG.DISPATCHER.add_handler(CommandHandler('start', start))