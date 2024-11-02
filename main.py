from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7487424620:AAGWN4wURfzbtA0ZQfVfcN2avax152sLSnQ')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    await message.answer('Privet, moi dryg!', reply_markup=markup)

executor.start_polling(dp)#функция которая не дают завершить работу бота
