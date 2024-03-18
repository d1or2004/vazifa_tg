from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menyu_keyword = ReplyKeyboardMarkup([
    [KeyboardButton("Front-end "), KeyboardButton("Beckent"), KeyboardButton("Settings")],
    [KeyboardButton("Admin haqida ma'lumot 😏")]
],
    resize_keyboard=True)

front1 = ReplyKeyboardMarkup([
    [
        KeyboardButton("HTML")
    ],
    [KeyboardButton("CSS")],
    [KeyboardButton("Javascipt")],
    [KeyboardButton("Back")]
],

    resize_keyboard=True)


def backend_btn():
    python = KeyboardButton(text='Python')
    java = KeyboardButton(text='Java')
    Csh = KeyboardButton(text='C#')
    bas = KeyboardButton(text='Back')
    return ReplyKeyboardMarkup([[python, java], [Csh], [bas]], resize_keyboard=True)


def admin_haqida():
    fish = KeyboardButton(text="Ma'lumot")
    talim = KeyboardButton(text="Ta'lim muassasi")
    baskk = KeyboardButton(text="Back")
    return ReplyKeyboardMarkup([[fish, talim], [baskk]], resize_keyboard=True)
