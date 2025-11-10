from aiogram.filters import Command  #Для бота
from aiogram.types.bot_command import BotCommand  #Для користувача



BOT_ENCRYPT_COMMAND = BotCommand(command="encrypt", description="Зашифрувати")
BOT_DECRYPT_COMMAND = BotCommand(command="decrypt", description="Розшифрувати")
BOT_SET_ALGORITHM_COMMAND = BotCommand(command="set_algorithm", description="Вибрати алгоритм")
BOT_HELP_COMMAND = BotCommand(command="help", description="Допомога")

ENCRYPT_COMMAND = Command("encrypt")
DECRYPT_COMMAND = Command("decrypt")
SET_ALGORITHM_COMMAND = Command("set_algorithm")
HELP_COMMAND = Command("help")