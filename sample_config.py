
   
import os


class Config(object):
    TG_BOT_TOKEN = "5358292714:AAHjSs7F1be2M5auG78sF6-zPVujPA0IJ-0"
    APP_ID = 9325118
    API_HASH = "5d3831feb6752d0a6904accac2008250"
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1123564262").split())
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", None)
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    DEF_THUMB_NAIL_VID_S = os.environ.get(
        "DEF_THUMB_NAIL_VID_S", ""
    ) # https://placehold.it/90x90
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    DEF_WATER_MARK_FILE = ""
    DATABASE_NAME = "LegendBot"
    DATABASE_URL = "mongodb+srv://LegendBoy:LegendBoy1234@cluster0.1kerb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
