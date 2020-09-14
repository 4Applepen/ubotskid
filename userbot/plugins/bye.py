

import time

from telethon.tl.functions.channels import LeaveChannelRequest
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("bye", outgoing=True))
async def bye(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit('**Esco dalla chat!**')
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('**Non puoi abbandonare la chat**')
