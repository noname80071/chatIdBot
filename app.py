from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from asyncio import run
import configparser
config = configparser.ConfigParser()
config.read("/etc/tgbot/settings.ini")
BOT_TOKEN = config["BOT"]["BOT_TOKEN"]
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
  await send_info(message)
@dp.message(Command('help'))
async def start(message: Message):
  await send_info(message)
async def send_info(message:Message):
  text = '\n'.join(("Ваши данные:",
                   f"chat id: {message.from_user.id}",
                   f"first name: {message.from_user.first_name}",
                   f"user name: {message.from_user.username}"))
  await message.answer(text)

async def main():
  await dp.start_polling(bot)

if __name__ == '__main__':
  run(main())