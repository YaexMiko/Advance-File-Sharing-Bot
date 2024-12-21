#(©)CodeXBotz




import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7244234428:AAHp9RXkP3ZGItu5lcwxf4r_d_jVnnPaPoA")  

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20071888"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1c4cb9d94b23282abd9ae2a87a521b53")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002409382999"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7592125322"))

#Port
PORT = os.environ.get("PORT", "2849")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ZeroTwo:aloksingh@zerotwo2.201lbx7.mongodb.net/?retryWrites=true&w=majority")
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DB_URI)
DB_NAME = os.environ.get("DATABASE_NAME", "madflixbotz")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start pic
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/de6a7340b530c2a71af37.jpg")

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>𝙷𝚎𝚕𝚕𝚘 {first}\n\n𝙸 𝙲𝚊𝚗 𝚂𝚝𝚘𝚛𝚎 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝚒𝚗 𝚂𝚙𝚎𝚌𝚒𝚏𝚒𝚎𝚍 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝚊𝚗𝚍 𝚘𝚝𝚑𝚎𝚛 𝚞𝚜𝚎𝚛𝚜 𝚌𝚊𝚗 𝚊𝚌𝚌𝚎𝚜𝚜 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝙵𝚛𝚘𝚖 𝚊 𝚂𝚙𝚎𝚌𝚒𝚊𝚕 𝙻𝚒𝚗𝚔....!</b>.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/de6a7340b530c2a71af37.jpg")


#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>𝚂𝚘𝚛𝚛𝚢 𝙳𝚞𝚍𝚎 𝚈𝚘𝚞 𝙽𝚎𝚎𝚍 𝚃𝚘 𝙹𝚘𝚒𝚗 𝚃𝚑𝚎𝚜𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜</b>\n\n<b>𝚂𝚘 𝙿𝚕𝚎𝚊𝚜𝚎 𝙲𝚕𝚒𝚌𝚔 𝙱𝚕𝚘𝚠 𝚃𝚘 𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 🔥</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", )

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ 𝙿𝚕𝚎𝚊𝚜𝚎 𝙰𝚟𝚘𝚒𝚍 𝙳𝚒𝚛𝚎𝚌𝚝 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜.<b>➥Tᴇᴀᴍ Hᴇᴀᴠᴇɴ \n─────────────────────────────────\n➥𝙸𝚏 𝚈𝚘𝚞 𝙷𝚊𝚟𝚎 𝙰𝚗𝚢 𝙿𝚛𝚘𝚋𝚕𝚎𝚖 𝚁𝚎𝚕𝚊𝚝𝚎𝚍 𝚃𝚘 𝙲𝚘𝚗𝚝𝚎𝚗𝚝 𝚃𝚑𝚊𝚝 𝚆𝚊𝚜 𝚁𝚎𝚖𝚘𝚟𝚎𝚍 𝙸𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙱𝚘𝚝 𝙸𝚜 𝙽𝚘𝚝 𝚆𝚘𝚛𝚔𝚒𝚗𝚐 𝙿𝚛𝚘𝚙𝚎𝚛𝚕𝚢 𝚃𝚑𝚎𝚗 𝚈𝚘𝚞 𝙲𝚊𝚗 𝙲𝚘𝚗𝚝𝚊𝚌𝚝 𝙷𝚎𝚛𝚎 𝙶𝚒𝚟𝚎𝚗 𝙱𝚎𝚕𝚘𝚠.\n➥𝙲𝚘𝚗𝚝𝚎𝚌𝚝 𝙾𝚠𝚗𝚎𝚛: @Heaven_Owner_Bot\n➥𝙲𝚘𝚗𝚝𝚎𝚌𝚝 𝙰𝚍𝚖𝚒𝚗: @Orignal_Owner_bot\n─────────────────────────────────</b>"

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
   
