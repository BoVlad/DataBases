from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot("8222927724:AAG4oJLzsnQ-X_9JflHfAzR6P79VYGaFcms")
dp = Dispatcher()
router = Router()
dp.include_router(router)

# --- Клава ---

def get_main_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [
            InlineKeyboardButton(text="👍 Нравится", callback_data="like"),
            InlineKeyboardButton(text="👎 Не нравится", callback_data="dislike"),
        ],
        [
            InlineKeyboardButton(text="❌ Закрыть", callback_data="close"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

# --- Хэндлеры ---

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Вот сообщение с кнопками:",
        reply_markup=get_main_keyboard()
    )

@router.callback_query(F.data == "like")
async def on_like(callback: CallbackQuery):
    # await callback.answer("Спасибо за лайк ❤️", show_alert=True)
    # можешь что-то сделать в коде:
    # например, изменить сообщение
    await callback.message.edit_text("Ты нажал 👍 Нравится")

@router.callback_query(F.data == "dislike")
async def on_dislike(callback: CallbackQuery):
    await callback.answer("Ок, учту 👌", show_alert=False)
    await callback.message.edit_text("Ты нажал 👎 Не нравится")

@router.callback_query(F.data == "close")
async def on_close(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()

# --- Запуск ---

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
