#(©)CodeXBotz




import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7917935047:AAGWfcJB490qPHEMobY6gwtG9CdONhZj5Y8")  

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20071888"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1c4cb9d94b23282abd9ae2a87a521b53")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002326266538"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "8108281129"))

#Port
PORT = os.environ.get("PORT", "2729")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Miko:aloksingh@miko.7c6wc.mongodb.net/?retryWrites=true&w=majority")
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DB_URI)
DB_NAME = os.environ.get("DATABASE_NAME", "Miko")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002281930837"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002281930837"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Pic
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/e726b0275bf54a4836803-465c1b6a0aa2fce275.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e726b0275bf54a4836803-465c1b6a0aa2fce275.jpg")

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b><Bold>➥ ʜᴇʟʟᴏ {first}\n\n➥ ɪ ᴀᴍ ᴘʟᴇᴀsᴇᴅ ᴛᴏ ɪɴғᴏʀᴍ ʏᴏᴜ ᴛʜᴀᴛ ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴄᴏɴᴛᴇɴᴛ ᴏғ ᴀɴɪᴍʀ ғɪʟᴇ ғʀᴏᴍ ʏᴏᴜʀ ғᴀᴠᴏᴜʀᴛᴇ ᴀɴɪᴍᴇ sᴇʀɪᴇs.\n➥ ʏᴏᴜ ʜᴀᴠᴇ ᴍᴀɴʏ ᴏᴘᴛɪᴏɴ ᴛᴏ sᴇʟᴇᴄᴛ ᴅɪғғᴇʀᴇɴᴛ ϙᴜᴀʟɪᴛʏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜ [480ᴘ, 720ᴘ 1080ᴘ, ʜᴅʀɪᴘ].\n\n➥ ᴛᴇᴀᴍ ᴡᴀʀʟᴏʀᴅs</Bold></b>.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/5a7094b992c50c7ecb1f7-7f41714fde1ac6b426.jpg")


#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><Bold>➥ ᴍʏ ᴅᴇᴀʀ sᴜʙsᴄʀɪʙᴇʀᴀ ʏᴏᴜ ᴅɪᴅ ɴᴏᴛ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛʜᴀᴛ ɢɪᴠᴇɴ ʙᴇʟʟᴏᴡ. \n\n➥ ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇ ᴛʜᴀᴛ ʏᴏᴜ ʀᴇϙᴜᴇsᴛᴇᴅ.</Bold></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", )

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b><bold>➥ ʜᴇʟʟᴏ ᴍʏ ᴅᴇᴀʀ sᴜʙsᴄʀɪʙᴇʀ ɪ ᴀᴍ ᴏɴʟʏ ғɪʟᴇ sʜᴀʀɪɴɢ ʙᴏᴛ ᴛᴏ ʜᴇʟᴘ ᴏᴛʜᴇʀ ʙʏ ɢɪᴠɪɴɢ ʀᴇϙᴜᴇsᴛᴀʙʟᴇ ᴄᴏɴᴛᴇɴᴛ. \n\n➥ ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴛʜᴀᴛ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ꜰᴏʀ ᴍᴏʀᴇ ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇ.\n➥ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴛᴇᴀᴍ ᴡᴀʀʟᴏʀᴅs @TeamWarlords</bold></b>"
ADMINS.append(OWNER_ID)
ADMINS.append(6446763201)

LOG_FILE_NAME = "filesharingbot.txt"

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
   
