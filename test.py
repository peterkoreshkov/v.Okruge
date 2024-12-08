import asyncio
from aiogram import Bot, types, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.fsm import state
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.types.web_app_info import WebAppInfo

TOKEN = '8184756910:AAHrjvfgZChQWajy7VlpBt7hMIJQuRgSSfE'
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
router = Router()
print('Bot started')


class user_settings(StatesGroup):
    button_name = State()


async def menu_keyboard():
    menu_keyboard = InlineKeyboardBuilder()
    menu_keyboard.button(text='Открыть', web_app=WebAppInfo(url='https://peterkoreshkov.github.io/v.Okruge/'))
    menu_keyboard.adjust(1)
    return menu_keyboard.as_markup()

@router.message(CommandStart())
async def start_menu(message: Message, state: FSMContext):
    await message.answer('Потапаем?', reply_markup=await menu_keyboard())


async def get_updates():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
asyncio.run(get_updates())