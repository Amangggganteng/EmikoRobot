import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/08fdbf96f37505efd36f2.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hai [{event.sender.first_name}](tg://user?id={event.sender.id}), Saya AMG-Robot.** \n\n"
  TEXT += " **Saya Bekerja Dengan Benar** \n\n"
  TEXT += f" **Juragan Ku : [ᴀᴍᴀɴɢ](https://t.me/mwahnq)** \n\n"
  TEXT += f" **Library Version :** `{telever}` \n\n"
  TEXT += f" **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f" **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Terima Kasih Telah Menambahkan Saya Di Sini ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/amanqss?start=help"), Button.url("Donasi", "https://t.me/mwahnq")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
