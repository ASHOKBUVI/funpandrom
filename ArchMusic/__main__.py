import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from FunX import LOGGER, app, userbot
from FunX.core.call import Fun 
from FunX.plugins import ALL_MODULES
from FunX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("FunX").error(
            "🙄 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 😐"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("FunX").warning(
            "🥲 𝐒𝐢𝐫 𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐈𝐝 & 𝐒𝐞𝐜𝐫𝐞𝐭 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝. 𝐃𝐨𝐧𝐭 𝐖𝐨𝐫𝐫𝐲 𝐍𝐨𝐭 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐄𝐧𝐣𝐨𝐲 𝐓𝐞𝐧𝐬𝐢𝐨𝐧 𝐅𝐫𝐞𝐞 🥰"
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("FunX.plugins." + all_module)
    LOGGER("FunX.plugins").info(
        "😋 𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲 🎉"
    )
    await userbot.start()
    await Fun.start()
    await Fun.decorators()
    LOGGER("FunX").info("╔═════۩۞۩════╗\n♨️𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐏𝐎𝐃𝐂𝐀𝐒𝐓♨️\n╚═════۩۞۩════╝")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("funX").info("😢 𝐒𝐨𝐫𝐫𝐲 𝐒𝐭𝐨𝐩𝐩𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 ☹️")
