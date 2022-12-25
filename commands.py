import random

from bot_config import dp, bot
from aiogram import types

s = random.randint(0, 1)
h = 0
d = 0


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    global s
    global h
    global total
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', привет! Добро пожаловать в игру!')
    if s == 0:
        await bot.send_message(message.from_user.id, text=f'Первым ходите вы')
    else:
        await bot.send_message(message.from_user.id, text=f'Первым ходит робот')
        h = random.randint(1, 27)
        await bot.send_message(message.from_user.id, f'Робот, взял со стола {h} конфет.')
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                     f', теперь ваш ход.')

total = 150 - int(h)

@dp.message_handler()
async def anything(message: types.Message):
    global total
    global d
    if total > 28:
        if message.text.isdigit():
            if 0 < int(message.text) < 29:
                total -= int(message.text)
                await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                             f', взял со стола {message.text} конфет.'
                                                             f'На столе осталось {total}')
                d = 1
                if total > 28:
                    h = random.randint(1, 27)
                    total -= int(h)
                    await bot.send_message(message.from_user.id, f'Робот, взял со стола {h} конфет.'
                                                                f'На столе осталось {total}')
                    if total > 28:
                        await bot.send_message(message.from_user.id, f'Теперь ходит {message.from_user.first_name}')
                        d = 0
                    else:
                        await bot.send_message(message.from_user.id, f'Победа за {message.from_user.first_name}!')

                else:
                    if d == 0:
                        await bot.send_message(message.from_user.id, f'Победа за {message.from_user.first_name}')
                    else:
                        await bot.send_message(message.from_user.id, f'Победил робот!')
            else:
                await message.reply(f'{message.from_user.first_name}, можно брать небольше 28 конфет!'
                                    f'{message.from_user.first_name}, ходи ещё раз')
