import logging
from aiogram import Bot, Dispatcher, executor,types
from aiogram.types import *
from database import *

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "6370077685:AAGqeKR8gsMkf0veqd2JjTzjgqKdBmRxA_4"

bot = Bot(token=BOT_TOKEN,parse_mode="html")
dp = Dispatcher(bot=bot)

async def  on_start_bot(dp):
    await create_tables()

@dp.message_handler(commands =["start"])
async def start_bot(message:types.Message):
    await message.answer("Salom")

@dp.message_handler(content_types=["audio"])
async def get_music(message:types.Message):
    music_name = message.audio.performer + " " + message.audio.title
    await insert_data(music_name,message.audio.file_id)


@dp.message_handler(commands=["top"]) 
async def get_all_music(message:types.Message):
    musics = await get_all_music()
    await message.answer("Toplam")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start_bot)

