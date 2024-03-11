from aiogram import Dispatcher, Bot, filters
from aiogram.types import Message
import asyncio
from oxfordLookUp import getDefinition
from googletrans import Translator

TOKEN = '6672189211:AAGNxANUPpZKsSPaqoQT3aphNPFbIlaz32s'
translator = Translator()
dp = Dispatcher()


@dp.message(filters.CommandStart())
async def startHandler(message: Message):
    await message.reply("hello! Welcome back")


@dp.message(filters.Command("help"))
async def helpHandler(message: Message):
    await message.reply("bu bot manolarni qidiradi")


@dp.message()
async def translateHandler(msg: Message):
    word = ''
    lang = translator.detect(msg.text).lang
    if len(msg.text.split()) > 2:
        dest = "uz" if lang == "en" else "en"
        await msg.reply(translator.translate(msg.text, dest).text)
    else:
        if lang == 'en':
            word = msg.text
        else:
            word = translator.translate(msg.text, dest='en').text

        lookup = getDefinition(word)
        if  lookup:
            await msg.reply(f"word: {word} \n definitions: \n{lookup['definitions']}")
            if  lookup.get('audio'):
                await msg.reply_audio(lookup['audio'])
        else:
            await msg.reply("bunday so'z topilmadi. Afsuuuuussss!!!!")



async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


asyncio.run(main())
