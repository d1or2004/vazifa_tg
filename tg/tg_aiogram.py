import logging
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from keywords import menyu_keyword, front1, backend_btn, admin_haqida
from main import Database
from inline_keywords.post import inline_keyword_1, inline_keyword_2

load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = message.chat.id
    check_query = f"""SELECT * FROM users WHERE chat_id = '{chat_id}'"""
    print(Database.connect(check_query, "select"))
    if len(Database.connect(check_query, "select")) == 1:
        await message.answer(f"Hi {message.chat.id}", reply_markup=menyu_keyword)
    else:
        print(f"{first_name} start bot")
        query = f"""INSERT INTO users(first_name, last_name, username, chat_id) VALUES('{first_name}','{last_name}','{username}','{chat_id}')"""
        print(f"{username} {Database.connect(query, 'insert')} database ")
        print(message.from_user.username)
        await message.answer(f"O'zingizga qiziq bo'lgan bo'limni tanlang", reply_markup=menyu_keyword)


@dp.message_handler(lambda massage: massage.text == "Front-end")
async def fron1(massage: types.Message):
    await massage.answer("Ma'lumot olmoqchi bo'lsangiz tanlang 👇", reply_markup=front1)


@dp.message_handler(lambda massage: massage.text == "Beckent")
async def bak_handler(massage: types.Message):
    await massage.answer("Ma'lumot olmoqchi bo'lsangiz tanlang 👇 ", reply_markup=backend_btn())


@dp.message_handler(lambda massage: massage.text == "Admin haqida ma'lumot 😏")
async def bak_handler(massage: types.Message):
    await massage.answer("Ma'lumot olmoqchi bo'lsangiz tanlang 👇 ", reply_markup=admin_haqida())


@dp.message_handler(lambda massage: massage.text == "Ma'lumot")
async def bak_handler(massage: types.Message):
    await massage.answer("Admin haqida\n |_ Ma'lumot _|", reply_markup=inline_keyword_1)


@dp.message_handler(lambda massage: massage.text == "Ta'lim muassasi")
async def bak_handler(massage: types.Message):
    await massage.answer("Ta'lim muassasi haqida \n |_ Ma'lumot _|", reply_markup=inline_keyword_2)


@dp.message_handler(lambda massage: massage.text == "HTML")
async def html(massage: types.Message):
    await massage.answer(
        f"""HTML tili taxminan 1991—1992-yillarda Yevropa Yadroviy Tadqiqotlar Markazida ishlovchi britaniyalik mutaxassis Tim Berners-Lee tomonidan ishlab chiqilgan. Dastlab bu til mutaxassislar uchun hujjat tayyorlash vositasi sifatida yaratilgan. HTML tilining soddaligi (SGMLga nisbatan) va yuqori formatlash imkoniyatlarining mavjudligi uni foydalanuvchilar orasida tez tarqalishiga sabab boʻldi. Bundan tashqari unda hipermatnlardan foydalanish mumkin edi. Tilning rivojlanishi bilan unga qo'shimcha multimedia (tasvir, tovush, animatsiya va boshqalar) imkoniyatlari qo'shildi.""""",
        reply_markup=front1)


@dp.message_handler(lambda massage: massage.text == "Javascipt")
async def fron1(massage: types.Message):
    await massage.answer(
        f"""JavaScript - bu interaktiv va dinamik veb-saytlarni yaratish uchun keng qo'llaniladigan dasturlash tili. U birinchi marta 1995 yilda Brendan Eich tomonidan ishlab chiqilgan va hozirda ECMAScript standartlari organi tomonidan qo'llab-quvvatlanadi. JavaScript barcha asosiy veb-brauzerlar tomonidan qo'llab-quvvatlanadigan yuqori darajali, talqin qilingan dasturlash tilidir.""""",
        reply_markup=front1)


@dp.message_handler(lambda massage: massage.text == "CSS")
async def bak_handler(massage: types.Message):
    await massage.answer(
        f"""CSS veb-sahifaning tashqi ko’rinishiga ishlov beradi. CSS dan foydalanib, siz matnning rangini,shriftlarning uslubini, paragraflar orasidagi bo’shliqni, ustunlarning o’lchamlari va joylashishini, fon rasmlari yoki ranglarning qanday ishlatilishini, sxemaning tuzilishini, turli xil qurilmalar va ekran o’lchamlari uchun displeyning o’zgarishini boshqarishingiz mumkin. shuningdek, turli xil effektlarni ham.""""",
        reply_markup=front1)


@dp.message_handler(lambda massage: massage.text == "Python")
async def bak_handler(massage: types.Message):
    await massage.answer(f"""Python nima?

Python - mashhur dasturlash tili. U Guido van Rossum tomonidan 1991 yilda ishlab chiqilgan.

Bu dasturlash tili o'rganish uchun oson, foydalanish uchun qulay, ko'p qirrali dasturlash tili bo'lib, dasturlashga yangi kirganlar uchun ham, soha mutaxassislari uchun ham zo'r tanlov.

Python quyidagilar uchun ishlatiladi:

* veb-ishlab chiqish (server tomonida),
* dasturiy ta'minotni ishlab chiqish,
* matematik amallar,
* tizim skriptlari.""", reply_markup=backend_btn())


@dp.message_handler(lambda massage: massage.text == "Java")
async def bak_handler(massage: types.Message):
    await massage.answer(
        f"""Java dasturlash tili 1991-yilda James Gosling, Patrick Naughton, Chris Warth, Ed Frank va Mike Sheridanlar tomonidan Sun Microsystems kompaniyasida yaratilgan. Tilning birinchi versiyasini yaratish uchun 18 oy vaqt ketgan. Bu til boshida „Oak“ (eman) deb nomlangan edi, lekin keyinchalik 1995-yilda „Java“ ga oʻzgartiligan. „Oak“ ning 1992-yilning kuz oylaridagi birinchi tadbiq etilishi va 1995-yilning bahorida „Java“ ning ommaga eʼlon qilinishidagi vaqt oraligʻida koʻplab odamlar bu tilning dizayni va evolyutsiyasiga oʻz hissalarini qoʻshishgan. Bil Joy, Arthur van Hoff, Jonathan Payne, Frakn Yellin va Tim Lindhom javaning asl prototipiga asosiy hissa qoʻshuvchilar hisoblanadi.""""",
        reply_markup=backend_btn())


@dp.message_handler(lambda massage: massage.text == "C#")
async def bak_handler(massage: types.Message):
    await massage.answer(
        f"""C# ning kelib chiqishi 2000-yillarga borib taqaladi. O’sha yillarda Microsoft ushbu dasturlash tilini o’zlari uchun yaratshdi. Dastlab C#, JavaScript bilan raqobatlashayotgan Java tillariga javob sifatida, ya’ni Microsoftning talabiga Java javob bera olamgani tufayli Microsoft Visual Studio 2002 bilan birglikda ishlab chiqilgan til edi. C# va Java ham dastlabki davrlardan tan olinishi uchun raqobatlashayotgan edi. Darhaqiqat, bu ikkisi bir biridan ancha ko’chirmachiliklar qildi, toki C# boshqa yo’nalishga o’tmaguniga qadar. Shundan so’ng C# kompyuter uchun dasturlar ishlab chiqarish bo’yicha xalqaro standart sifatida tasdiqlandi va umumiy til infrastrukturasi bilan ishlatiladi.""""",
        reply_markup=backend_btn())


@dp.message_handler(lambda massage: massage.text == "Back")
async def bakc1(massage: types.Message):
    await massage.answer("O'zingizga kerakli b'limni tanlang  ", reply_markup=menyu_keyword)


@dp.message_handler(lambda massage: massage.text == "Settings")
async def settingiz(massage: types.Message):
    await massage.answer("|  Hozircha ma'lumotlar yo'q | ! ", reply_markup=menyu_keyword)


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    photo_url = (
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.texnoman.uz%2Fuploads%2Fblogs%2Fab2b41de1b1decadd01cca532ce1ce68.png&tbnid=h0oQl4nwxDXbGM&vet=12ahUKEwiE7vqX6_iEAxX8HBAIHb3kACcQMygEegQIARBR..i&imgrefurl=https%3A%2F%2Fwww.texnoman.uz%2Fpost%2Fnima-uchun-python-dasturlash-tilini-organish-kerak-5ta-sabab_.html&docid=DHZkikKrR4ls3M&w=840&h=500&q=python%20nima&ved=2ahUKEwiE7vqX6_iEAxX8HBAIHb3kACcQMygEegQIARBR")
    caption = 'Siz izlagan rasm'
    await bot.send_photo(message.chat.id, photo=photo_url, caption=caption)


@dp.message_handler(commands=['admin'])
async def admin_command(message: types.Message):
    if message.from_user.id in [6248642122]:
        await message.reply("Salom Diyorbek")
    else:
        await message.reply("Bu buyruq faqat adminla uchun")


#
# @dp.message_handler(commands=['data'])
# async def select(message: types.Message):
#     query_select = f"""SELECT * FROM users where chat_id = '{chat_id}'"""
#     data = Database.connetc(query_select, "select")
#
#     await message.reply(data)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
