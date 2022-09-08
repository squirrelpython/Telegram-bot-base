from bot_base import CONFIG



if __name__ == "__main__":
    CONFIG.load_modules()
    CONFIG.UPDATER.start_polling()
    CONFIG.UPDATER.idle()