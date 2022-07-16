
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", ""))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "no").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "BQC3Wbx1ah8TiPyWKyO7dmk08HjCYLGgqvlNM1VCfl5htfqc0pZml-UCedPS4RxwDZ7oEozTRwCaJnPPr2xmNteDwb0e1kOC4P_npYauss4HyIClYDQt1E-h7ajsU12AgXYre1YqR4FHZwsk-HPR3TaAnUomQyjCVrjt0YnFZ2T7uuwhvDZXGYQLGITPj_AYyhel1R_GWocha5VwFPfln8fl2fd3LIw33VjLPZ8k5btkF9GIGonzwOOUJ_IYovg9U8l6frknmlSfepmBccL5jRppOzB9ZiwLvdI4leOGjPYgUF97r3XHh8KRysIRr_Ib8IQ7lAazST833H71ifOo1k_AAAAAACOLYaUA")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

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
