from mailbox import Message

import telebot
from telebot import types

bot = telebot.TeleBot('1314188183:AAHb_EmLam3dPet1SJnwaYlXcZFO8eEUVRs')
STICKER_ID = 'CAACAgIAAxkBAAMpXwQ68LQDnCu0uyjMbrY_c3-6OBcAAlgXAAJxzH0Y4VVKisA3h_oaBA'
@bot.message_handler(commands=['start'])
def start_handler(message: Message):
    bot.send_message(message.chat.id,'Привет от музыкального бота \n введите команду /help для получения большей информации')

@bot.message_handler(commands=['help'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, 'Я бот с быстрым доступом к трекам из Devil May Cry \n Введите команду /choose. Выберите игру,а после трек который хотите послушать.')


@bot.message_handler(commands=['choose'])
def choose_track(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btnDMC5 = types.KeyboardButton('DMC 5')
    btnDMC4 = types.KeyboardButton('DMC 4')
    btnDMC3 =types.KeyboardButton('DMC 3')
    markup.add(btnDMC5,btnDMC4,btnDMC3)
    bot.send_message(message.chat.id, "Выберите игру", parse_mode='html', reply_markup=markup)


def SendSound(video, audio, message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Слушать на YouTube", url=video,))
    bot.send_message(message.chat.id, "Отличный выбор", parse_mode='html', reply_markup=markup)
    bot.send_audio(message.chat.id, audio=audio)


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def lalala(message: Message):
    if 'The Time Has Come' in message.text:
        SendSound("https://www.youtube.com/watch?v=cLBAFJWbd30",
                  "https://mp3-youtube.download/download/access/20200708095046_2c404183-f60d-4598-be76-2d6bdd87bbab"
                  "?expires=1594202155&signature=5761f2a85b8046fd0a21a60fb38b5a4719da63be1c731865e06f81afb4ed4847 ",
                  message)
    if 'Lock and Load'in message.text:
        SendSound("https://www.youtube.com/watch?v=84jrCjX022Y",
                  "https://mp3-youtube.download/download/access/20200708094738_fd609dc1-8f70-4ef2-bfa0-59e85d4b7177"
                  "?expires=1594201970&signature=12cb5498a2654f2aac56c753568b103fbee195f1c9ac9c00b760a9f80c192839",
                  message)

    if'Shall Never Surrender' in message.text:
        SendSound("https://www.youtube.com/watch?v=PL8vLtyeU7Y",
                  "https://mp3-youtube.download/download/access/20200708094510_cd77d859-1861-4ed8-98dc-2f4eb4f2953a"
                  "?expires=1594201820&signature=cda26f936f52625fea4ed892da7c65997cd8d4127ce6f85c06e60c7662c463c2",
                  message)

    if'Subhuman'in message.text:
        SendSound("https://www.youtube.com/watch?v=2Sb7chMVrh4",
                  "https://mp3-youtube.download/download/access/20200708093046_421bcd3e-9bab-4ed1-b744-8f637f72d0de"
                  "?expires=1594201121&signature=f4dfabd0839787cf991edfd6a69d3343779093c39a178aa9a194125c476b9f92",
                  message)

    if 'Crimson Cloud' in message.text:
        SendSound("https://www.youtube.com/watch?v=51_1zQg2k6s",
                  "https://mp3-youtube.download/download/access/20200708091746_7a1ba044-70cd-415c-b369-f6fab91d7367"
                  "?expires=1594200176&signature=e899e9a010330d742cf50ca1b224bb2bc81c77b4cffa00e528aa7607f4644eac",
                  message)

    if 'Devil Trigger' in message.text:
        SendSound("https://youtu.be/-WpnPSChVRQ",
                  "https://cdn.downloadmaster.cc/download.php?id=-WpnPSChVRQ&method=download&title=["
                  "Full%20Song/Official%20Lyrics]%20Devil%20Trigger%20-%20Nero%27s%20battle%20theme%20from%20Devil"
                  "%20May%20Cry%205&token=353f49c4787eaf1c21a008960122678540f4fec4",
                  message)

    if 'Devils Never Cry' in message.text:
         SendSound("https://www.youtube.com/watch?v=GZUN89RaP60",
                   "https://mp3-youtube.download/download/access/20200709134555_8430374c-b21c-4dc8-80f0-5ed890d39fab"
                   "?expires=1594302665&signature=d0eeb32223199483e4a1943ac125a5f10b73a7c31100c5666d92b7a7f297ba62",
                   message)

    if 'Taste The Blood'in message.text:
        SendSound("https://www.youtube.com/watch?v=5mhYtdvOuD8",
                  "https://mp3-youtube.download/download/access/20200709134653_d623f0ac-887a-4ddf-ad6c-835e32800568"
                  "?expires=1594302722&signature=b014eebf81a70746a66a17633ce99ba53b2fbfaaee8ff3d6c0c3a858e6f7ce77",
                  message)

    if 'Crossed the line' in message.text:
        SendSound("https://www.youtube.com/watch?v=l9euq6kJL_A",
                  "https://mp3-youtube.download/download/access/20200709133930_bcc7a03b-3438-4536-98fa-fa8479fe9b7a"
                  "?expires=1594302278&signature=e09576f8595f98eab6b6df5da10653e22eb833acc315cde1bf368fee0e9f6bb4",
                  message)

    if 'DMC 3' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btnDevilsNeverCry = types.KeyboardButton('Devils Never Cry')
        btnTasteTheBlood = types.KeyboardButton('Taste The Blood')
        btnCrossedTheLine = types.KeyboardButton('Crossed the line')
        markup.add(btnDevilsNeverCry,btnTasteTheBlood,btnCrossedTheLine)
        bot.send_message(message.chat.id, "Выберите трек", parse_mode='html', reply_markup=markup)

    if 'DMC 4' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btnShallNeverSurrender = types.KeyboardButton('Shall Never Surrender')
        btnLockAndLoad = types.KeyboardButton('Lock and Load')
        btnTheTimeHasCome = types.KeyboardButton('The Time Has Come')
        markup.add(btnShallNeverSurrender,btnLockAndLoad,btnTheTimeHasCome)
        bot.send_message(message.chat.id, "Выберите трек", parse_mode='html', reply_markup=markup)

    if 'DMC 5' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btnDevilTrigger = types.KeyboardButton('Devil Trigger')
        btnCrimsonCloud = types.KeyboardButton('Crimson Cloud')
        btnSubhuman = types.KeyboardButton('Subhuman')
        markup.add(btnDevilTrigger, btnCrimsonCloud, btnSubhuman)
        bot.send_message(message.chat.id, "Выберите трек", parse_mode='html', reply_markup=markup)
    if 'DMC 4' not in message.text and 'DMC 5' not in message.text and 'DMC 3' not in message.text:
        bot.send_message(message.chat.id, 'I NEED MORE POWER')


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, STICKER_ID)


# RUN
bot.polling(none_stop=True)
