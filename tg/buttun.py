from aiogram import types

keyboard = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton(text="Option 1", callback_data="option1")
button2 = types.InlineKeyboardButton(text="Option 2", callback_data="option2")
keyboard.add(button1, button2)
