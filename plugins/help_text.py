import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation
from helper_funcs.forcesub import ForceSub
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.HELP_USER,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    #forcesub = await ForceSub(bot, update)
    #if forcesub == 400:
        #return
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "sᴜᴘᴘᴏʀᴛ", url="https://t.me/TeleRoid14"
                        ),
                        InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/TeleRoidGroup"),
                    ],
                    [InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/TheTeleRoid")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
