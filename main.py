import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6025864995:AAHm6vJUnX_KFI17E1LFceI4M1VyZRMGcaY'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

Matematika_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Matematika"),
            # KeyboardButton(text="Tarix"),
            # KeyboardButton(text="Ona tili")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom. Men viktorinabotman.",reply_markup=Matematika_menu_keyboard)





@dp.message_handler(text="Matematika")
async def echo(message: types.Message):
    # 1 - misol
    await message.answer_poll(
        question="8 * 8 =",
        options=["64", "58", "44"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)

    # 2 - misol
    await message.answer_poll(
        question="44 * 17 =",
        options=["340", "748", "980"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(3)

    # 3 - misol
    await message.answer_poll(
        question="97 * 8 =",
        options=["646", "884", "776"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(3)

    # 4 - misol
    await message.answer_poll(
        question="1546 - 738 =",
        options=["908", "808", "624"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(3)

    # 5 - misol
    await message.answer_poll(
        question="4890 + 822 =",
        options=["6422", "5855", "5712"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(3)

    # 6 - misol
    await message.answer_poll(
        question="449 - 223 =",
        options=["672", "226", "712"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(3)

    # 7 - misol
    await message.answer_poll(
        question="90 * 22 =",
        options=["1890", "5855", "5712"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)

    # 8 - misol
    await message.answer_poll(
        question="48 / 8 =",
        options=["6", "5", "7"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)

    # 9 - misol
    await message.answer_poll(
        question="999 + 567 =",
        options=["6422", "1566", "5712"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(3)

    # 10 - misol
    await message.answer_poll(
        question="9 * 822 =",
        options=["6422", "5855", "7398"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(3)








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    















# @dp.message_handler(text="s")
# async def echo(message: types.Message):
#     await message.answer_poll(
#         question="Kim yaxshi",
#         options=["Olim", "Hakim", "Tohir", "Eldor"],
#         is_anonymous=False
#     )
#     await asyncio.sleep(5)

#     await message.answer_poll(
#         question="Kim yaxshi",
#         options=["Olim", "Hakim", "Tohir", "Eldor"],
#         is_anonymous=False
#         correct_option_id=1,
#         type="quiz"
#     )
#     await asyncio.sleep(5)


    # await message.answer_poll(
    #     question="Kim yaxshi",
    #     options=["Olim", "Hakim", "Tohir", "Eldor"],
    #     is_anonymous=False
    # )

# @dp.message_handler(text="o")
# async def echo(message: types.Message):
#     await message.answer_poll(
#         question="Kim yaxshi",
#         options=["Olim", "Hakim", "Tohir", "Eldor"],
#         is_anonymous=False,
#         allows_multiple_answers=True
#     )