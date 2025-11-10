from aiogram.fsm.state import State, StatesGroup

class Encrypt(StatesGroup):
    mess_to_en = State()
    shift_to_en = State()

class Decrypt(StatesGroup):
    mess_to_dec = State()
    shift_to_dec = State()