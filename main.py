from aiogram.utils import  executor
from commands import dp

async def bot_start(_):
    print('Бот запущен!')

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True, on_startup=bot_start)


# import random
#
# s = random.randint(0, 1)
# print(s)
# z = 150
# if s == 0:
#     print('Первым ходите вы')
#     print(f'Всего конфент {z}')
#     d = int(input('Введите колличестов конфет: '))
#     z = z - d
#     print(f'Конфет осталось {z}')
#     s = 1
# else:
#     print('Первый ход за компьютером')
#     print(f'Всего конфент {z}')
#     h = random.randint(1, 28)
#     print(f' Компьютер взял {h} конфет')
#     z = z - h
#     print(f'Конфет осталось {z}')
#     s = 0
# while z > 28:
#     if s == 0:
#         d = int(input('Введите колличестов конфет: '))
#         z = z - d
#         print(f'Конфет осталось {z}')
#         s = 1
#     else:
#         h = random.randint(1, 28)
#         print(f' Компьютер взял {h} конфет')
#         z = z - h
#         print(f'Конфет осталось {z}')
#         s = 0
# else:
#     if s == 0:
#         print('Победили вы !!!!')
#     else:
#         print('Победил компьтер !!!!!!')