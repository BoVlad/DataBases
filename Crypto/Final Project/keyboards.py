from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def cmd_set_algorithm_keyboard(items: dict) -> InlineKeyboardMarkup:
    keyboard = [[]]
    column_counter = 1
    index_counter = 0
    for key, value in items.items():
        if column_counter == 1:
            keyboard[index_counter].append(InlineKeyboardButton(text=key, callback_data=f"btn1:{value}"))
            column_counter = 2
        elif column_counter == 2:
            keyboard[index_counter].append(InlineKeyboardButton(text=key, callback_data=f"btn1:{value}"))
            column_counter = 1
            index_counter += 1
            keyboard.append([])
    keyboard.append([InlineKeyboardButton(text="❌ Закрити", callback_data="btn1:close")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
