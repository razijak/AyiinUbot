from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


class Var:
    API_HASH = getenv("API_HASH""f578d564f0797fd5980db4727c7af359")
    API_ID = int(getenv("API_ID", "28745974"))
    ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/9f8e73d387f25b7f27ce5.jpg")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "Hey, Saya AyiinUbot Dibuat dengan basis pyrogram versi terbaru")
    BOT_TOKEN = getenv("BOT_TOKEN", "5850158151:AAGAbpEoeOH_VG5EKnhPMIiMZ3fu8eNOjLs")
    BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1001473548283, -1001675396283]
    LOG_CHAT = int(getenv("LOG_CHAT","-822425701" ) or 0)
    HNDLR = getenv("HNDLR", [".", "!", "*", "^", "-", "?"])
    DB_URL = getenv("DATABASE_URL", "")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    MONGO_URI = getenv("MONGO_URI", None)
    NO_LOAD = [int(x) for x in getenv("NO_LOAD", "").split()]
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "WEnHwQnst3E2HzjGgwmy4UpB")
    STRING_1 = getenv("STRING_1", "BQG2oPYAlTnR55D8GVjpU4fCZQSK4XWcZHOynUJKFW76DYCsvO2qaH2yGKooP1Ok9t1szaXM0UwQifHE_4JTc1rLW6CRonIIBXBO7yXPCv_-fXFJSwmfpShd_IzWAOUJPHnwRcWLNKr8xFsRpzk4Eq2FLwDMpnEGhsnDFpJIf8UXhcGMaKjy9qq-M62CqrJIDfA8XWZQDA072z65O_gVBw87twSQGEh99Nm97f8xMEfSvnFZJj0iMu9f2kVHEo-NgsAoapiaF2VCdy_15un-M5VhPsHjsWn5lbOleNgegEsw2bqu4SPu_NlpYjzGVY58Qn3grl0Mi-HD0JqKVsCN3MWDIi3AgAAAAAFTvI38AA")
    STRING_2 = getenv("STRING_2", "")
    STRING_3 = getenv("STRING_3", "")
    STRING_4 = getenv("STRING_4", "")
    STRING_5 = getenv("STRING_5", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
    TZ = getenv("TZ", "Asia/Jakarta")
