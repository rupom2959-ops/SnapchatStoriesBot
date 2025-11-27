import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "39462658"))
    API_HASH = os.environ.get("API_HASH", "adf62bcfbfa61b8a7374b0e792251a26" ))
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8218254427:AAFnXHxioyOV3tbs7jUPOmoYpelVZYi7HQw")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "tirreceiverbot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
