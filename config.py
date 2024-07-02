import sys
import os
import logging
from logging.handlers import RotatingFileHandler


from dotenv import load_dotenv

load_dotenv("config.env")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7280404452:AAHcCyl1m9Dm9MmLuwzavmxV67xSvKd9_2o")
APP_ID = int(os.environ.get("APP_ID", "29486311"))
API_HASH = os.environ.get("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001950756152"))
OWNER_ID = int(os.environ.get("OWNER_ID", "1707380693"))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kikoy:kikoy6969@cluster0.vooxu.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "debesub")
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001955926976"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001710331413"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002087078793"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "Hallo {first}\n\nsaya bisa menyimpan file dan membagikan dengan mudah.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1707380693").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hallo {first}\n\n<b>anda harus bergabung ke Channel/Group saya dulu untuk bisa melihat konten ini\n\nJoin Channel/group</b>")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False
try:
    import geezlibs
except ModuleNotFoundError:
    print("GeezLibs not installed, you are gay")
    sys.exit()
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Jangan kirimkan saya pesan!"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "geezfsub.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
