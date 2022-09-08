from telegram.ext import *
from telegram import *
from dotenv import load_dotenv
from os import environ
from importlib import import_module
from pymodm import connect
import logging


class Config:
    def __init__(self) -> None:
        # Load env config
        load_dotenv('config.env')
        logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
        self.LOGGER = logging.getLogger(__name__)
        self.BOT_TOKEN: str = environ.get('BOT_TOKEN')
        self.MONGO_URL: str = environ.get('MONGO_URL')
        self.MONGO_DB: str = environ.get('MONGO_DB')
        self.POSTGRESQL_URL: str = self.parse_url(environ.get('POSTGRESQL_URL'))
        self.UPDATER: Updater
        self.DISPATCHER: Dispatcher
        
    def parse_url(self, url: str):
        if url.startswith('postgres'):
            return url.replace('postgres', 'postgresql', 1)
        return url

    def load_modules(self):
        import_module(f'{__package__}.modules')


CONFIG = Config()
CONFIG.UPDATER = Updater(token=CONFIG.BOT_TOKEN, defaults=Defaults(
        run_async=True, # To run commands asynchronously
        disable_web_page_preview=True, # To disable web preview
        parse_mode='MARKDOWN' # to set parse_mode to markdown
))
CONFIG.DISPATCHER = CONFIG.UPDATER.dispatcher
connect(mongodb_uri=CONFIG.MONGO_URL, databse_name=CONFIG.MONGO_DB)

