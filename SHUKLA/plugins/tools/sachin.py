import os
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from ... import app, SUDO_USER
from ... import *
from SHUKLA.modules.SHASHANK.data import Sachin


FC = 2


@app.on_message(cdz(["CHHINNAR"])  & (filters.me | filters.user(SUDO_USER)))
async def alt_lol(xspam: Client, message: Message):    
    chat_id = message.chat.id
    RUSH = None
    if message.reply_to_message:
        RUSH = message.reply_to_message.id
    try:
        for word in Sachin:
            await xspam.send_message(chat_id, word, reply_to_message_id=RUSH)
            await asyncio.sleep(1)
    except FloodWait:
        print("Flood !!")
        pass



@app.on_message(cdz(["CHHINNARR"])  & (filters.me | filters.user(SUDO_USER)))
async def alt_mkc(xspam: Client, message: Message):    
    chat_id = message.chat.id
    RUSH = None
    if message.reply_to_message:
        RUSH = message.reply_to_message.id
    try:
        for word in Sachin:
            await xspam.send_message(chat_id, word, reply_to_message_id=RUSH)
            await asyncio.sleep(000.1)
    except FloodWait:
        print("Flood !!")
        pass
    
    

@app.on_message(cdz(["CCHHINAR"])  & (filters.me | filters.user(SUDO_USER)))
async def alt_stop(_, message: Message):    
    reply = await message.reply_text("MADRCHODD CHHINNAR...")
    await reply.edit("4ST OP BAKI SAB LAND KI TOPI \n\n SAMJHA RANDI KE CHODE")
    os.system(f"kill -9 {os.getpid()} && python3 -m SHUKLA")
    
