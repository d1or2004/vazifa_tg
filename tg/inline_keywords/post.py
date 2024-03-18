from aiogram import types

inline_keyword_1 = types.InlineKeyboardMarkup(row_width=3)
familiya = types.InlineKeyboardButton(
    text="Familiya: Axmadjonov  ",
    callback_data="option1")
ism = types.InlineKeyboardButton(
    text="Ism : Diyorbek",
    callback_data="option2")
username = types.InlineKeyboardButton(
    text="Username : _d1_or : )",
    callback_data="option3")
nomer = types.InlineKeyboardButton(
    text="Nomer : +998937777874",
    callback_data="option4")
inline_keyword_1.add(familiya, ism, username, nomer)

inline_keyword_2 = types.InlineKeyboardMarkup(row_width=3)
inline_keyword_2.add(types.InlineKeyboardButton("Ta'lim muassasi: O'zMU ", callback_data="option5"))
inline_keyword_2.add(types.InlineKeyboardButton("Kursi : 2 ", callback_data="option6"))
inline_keyword_2.add(types.InlineKeyboardButton("Fakultet : AMIT ", callback_data="option7"))
inline_keyword_2.add(types.InlineKeyboardButton("Yo'nalishi : Axborot havfsizligi  ", callback_data="option7"))
