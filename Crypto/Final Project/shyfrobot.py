import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher, html, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from config import BOT_TOKEN
from commands import (BOT_ENCRYPT_COMMAND, BOT_DECRYPT_COMMAND, BOT_SET_ALGORITHM_COMMAND, BOT_HELP_COMMAND,
                      ENCRYPT_COMMAND, DECRYPT_COMMAND, SET_ALGORITHM_COMMAND, HELP_COMMAND)
from keyboards import cmd_set_algorithm_keyboard
from default_ciphers import default_ciphers_dict, default_ciphers_dict_invert, caesar_cipher, masson_cipher_enc, masson_cipher_dec
from state import Encrypt, Decrypt
from file_utilts import *

files_name = ["users_data.json"]

TOKEN = BOT_TOKEN

dp = Dispatcher()
router = Router()
dp.include_router(router)

start_files(files_name)

@router.message(CommandStart())
async def cmd_start(message: Message):
    logging.info(f"{message.from_user.full_name}")
    await message.answer(f"Вітаю {html.bold(message.from_user.full_name)}!\n"
                         f"Я бот-шифрувальник для ваших повідомлень!")

@router.message(HELP_COMMAND, StateFilter("*"))
async def cmd_help(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Shyfro - це бот-шифрувальник для ваших повідомлень.\n\n"
                         "Команди:\n"
                         "• /encrypt - команда для шифрування (спочатку потрібно обрати алгоритм)\n"
                         "• /decrypt - команда для розфрування (спочатку потрібно обрати алгоритм)\n"
                         "• /set_algorithm - команда для обирання алгоритму\n", reply_markup=ReplyKeyboardRemove())

@router.message(SET_ALGORITHM_COMMAND, StateFilter("*"))
async def cmd_set_algorithm(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "🙊 Виберіть алгоритм:",
        reply_markup=cmd_set_algorithm_keyboard(default_ciphers_dict)
    )

@router.callback_query(F.data.startswith("btn1:"))
async def cmd_btn1_action(callback: CallbackQuery):
    await callback.message.delete()
    if callback.data.split("btn1:", maxsplit=1)[1] == "close":
        await callback.answer()
        return
    else:
        user_id = str(callback.from_user.id)
        algorithm = callback.data.split("btn1:", maxsplit=1)[1]

        data = load_data(files_name[0])
        data[user_id] = algorithm
        save_data(data, files_name[0])

        await callback.message.answer(f"Успішно вибрано алгоритм: {default_ciphers_dict_invert.get(algorithm)}")
        await callback.answer()


@router.message(ENCRYPT_COMMAND, StateFilter("*"))
async def cmd_encrypt(message: Message, state: FSMContext):
    await state.clear()
    file_data = load_data(files_name[0])
    user_id = str(message.from_user.id)
    try:
        error = file_data[user_id]
        await message.answer("Введіть текст для шифрування:", reply_markup=ReplyKeyboardRemove())
        await state.set_state(Encrypt.mess_to_en)
    except KeyError:
        await message.answer("❌ Не обран алгоритм шифрування", reply_markup=ReplyKeyboardRemove())

@router.message(Encrypt.mess_to_en)
async def mess_to_en(message: Message, state: FSMContext):
    await state.update_data(mess_to_en=str(message.text))

    file_data = load_data(files_name[0])
    user_id = str(message.from_user.id)

    if file_data[user_id] == "caesar_cipher":
        await state.set_state(Encrypt.shift_to_en)
        await message.answer('Введіть зміщення (наприклад: "3" - зміщення вправо на 3, "-3" - зміщення вліво на 3):',
                             reply_markup=ReplyKeyboardRemove())
    elif file_data[user_id] == "masson_cipher":
        data = await state.get_data()
        ciphered_message = masson_cipher_enc(data["mess_to_en"])
        await message.answer("Ось ваш шифр:")
        await message.answer(ciphered_message, parse_mode=None)
        await state.clear()
    else:
        await state.clear()

@router.message(Encrypt.shift_to_en)
async def shift_to_en(message: Message, state: FSMContext):
    try:
        val = int((message.text or "").strip())
    except (ValueError, TypeError):
        await message.answer("❌ Ви не ввели число. Спробуйте ще раз.")
        return
    await state.update_data(shift_to_en=val)

    data = await state.get_data()
    ciphered_message = ""

    file_data = load_data(files_name[0])
    user_id = str(message.from_user.id)

    if file_data[user_id] == "caesar_cipher":
        ciphered_message = caesar_cipher(data["mess_to_en"], data["shift_to_en"])
    await message.answer("Ось ваш шифр:")
    await message.answer(ciphered_message, parse_mode=None)
    await state.clear()

@router.message(DECRYPT_COMMAND, StateFilter("*"))
async def cmd_decrypt(message: Message, state: FSMContext):
    await state.clear()
    file_data = load_data(files_name[0])
    user_id = str(message.from_user.id)
    try:
        error = file_data[user_id]
        await message.answer("Введіть текст для дешифрування:", reply_markup=ReplyKeyboardRemove())
        await state.set_state(Decrypt.mess_to_dec)
    except KeyError:
        await message.answer("❌ Не обран алгоритм шифрування", reply_markup=ReplyKeyboardRemove())


@router.message(Decrypt.mess_to_dec)
async def mess_to_dec(message: Message, state: FSMContext):
    await state.update_data(mess_to_dec=str(message.text))
    file_data = load_data(files_name[0])
    user_id = str(message.from_user.id)

    if file_data[user_id] == "caesar_cipher":
        await state.set_state(Decrypt.shift_to_dec)
        await message.answer('Введіть зміщення (наприклад: "3" - зміщення вправо на 3, "-3" - зміщення вліво на 3):',
                             reply_markup=ReplyKeyboardRemove())
    elif file_data[user_id] == "masson_cipher":
        data = await state.get_data()
        deciphered_message = masson_cipher_dec(data["mess_to_dec"])
        await message.answer("Ось ваш шифр:")
        await message.answer(deciphered_message, parse_mode=None)
        await state.clear()
    else:
        await state.clear()

@router.message(Decrypt.shift_to_dec)
async def shift_to_dec(message: Message, state: FSMContext):
    try:
        val = int((message.text or "").strip())
    except (ValueError, TypeError):
        await message.answer("❌ Ви не ввели число. Спробуйте ще раз.")
        return
    val = -val
    await state.update_data(shift_to_dec=val)

    file_data = load_data(files_name[0])
    user_id = str(message.from_user.id)
    data = await state.get_data()
    deciphered_message = ""
    if file_data[user_id] == "caesar_cipher":
        deciphered_message = caesar_cipher(data["mess_to_dec"], data["shift_to_dec"])
    await message.answer("Ось ваша розшифровка:")
    await message.answer(deciphered_message, parse_mode=None)
    await state.clear()



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.set_my_commands(
        [
            BOT_ENCRYPT_COMMAND,
            BOT_DECRYPT_COMMAND,
            BOT_SET_ALGORITHM_COMMAND,
            BOT_HELP_COMMAND
        ]
    )

    # And the run events dispatching
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
