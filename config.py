import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7099461621:AAHXFf2xq5Il41WD2Q-fOlMQXzCS3e3_9QQ")
    APP_ID = int(os.environ.get("APP_ID", 23004101))
    API_HASH = os.environ.get("API_HASH")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
