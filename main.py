# number = 23
# running = True
#
# while running: # Цикл while с условием исполнения
#     guess = int(input('Введите целое число: '))
#
#     if guess == number:
#         print('Вы угадали')
#         running = False
#     elif guess < number:
#         print('Число меньше указанного')
#     else:
#         print('Число больше указанного')
# else:
#     print('Цикл while окончен')
#
# print('Завершение')
# ________________________________________________________________


# for i in list(range(5)):  # Цикл for c range()
#     print(i)
# else:
#     print('Цикл завершен')
# ________________________________________________________________


# while True: # Цикл while с break
#     s = input('Введите что-нибудь: ')
#     if s == 'exit':
#         break
#     else:
#         print('Длина строки:', len(s))
# print('Завершение')
# ________________________________________________________________


# while True: # Цикл while с continue
#     s = input('Enter something: ')
#     if s == 'exit':
#         break
#     if len(s) < 3:
#         print('Very little')
#         continue
#     print('The string you entered is long enough')
# # ________________________________________________________________


# def say_hello(): # Функция
#     print('Привет, мир!')
#     print('Привет, мир!')
#
#
# say_hello()
# ________________________________________________________________


# def print_max(a, b):  # Функции с вводом данных
#     if a > b:
#         print(a,'максимально')
#     elif a == b:
#         print(a, 'равно', b)
#     else:
#         print(b, 'максимально')
#
# print_max(3, 4)
#
# x = 5
# y = 7
#
# print_max(x, y)
# ________________________________________________________________


# Локальные переменные
# x = 50
#
# def func(x):
#     print('x равен', x)
#     x = 2
#     print('Замена локального х на ', x)
#
# func(x)
# print('x по прежнему', x)
# ________________________________________________________________


# Зарезервированное слово global - внутри функции значение переменной заменяет значение глобальной переменной

# x = 50
#
# def func():
#     global x
#
#     print('x равно', x)
#     x = 2
#     print('Заменяем глобальное значение х на', x)
#
# func()
# print('Значение х равно', x)
# ____________________________________________________________________


# Ключевые аргументы функции
#
# def func(a, b=5, c=10):
#     print('а равно', a, 'b равно', b, 'с равно', c)
#
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)
# ________________________________________________________________


# Переменное число параметров
#
# def total(a=5, *numbers, **phonebook):
#     print('a', a)
#
#     # Проход по всем элементам кортежа
#     for single_item in numbers:
#         print('single_item', single_item)
#
#     for first_part, second_part in phonebook.items():
#         print(first_part, second_part)
#
# total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)
# ____________________________________________________________________


# Оператор return - используется для возврата из функции
#
# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'Числа равны'
#     else:
#         return y
#
#
# print(maximum(2, 3))
# ________________________________________________________________________


# DocString - строки документации
#
# def print_max(x, y):
#     '''Выводит максимальное из двух чисел.
#     Оба значения должны быть целыми числами.'''
#     # конвертируем в целые если возможно
#     x = int(x)
#     y = int(y)
#
#     if x > y:
#         print(x, 'наибольшее')
#     else:
#         print(y, 'наибольшее')
#
#
# print_max(7, 9)
# print(print_max.__doc__)
# __________________________________________________________________




# Модули
#
# import sys
#
# print('Аргументы командной строки:')
# for i in sys.argv:
#     print(i)
#
# print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')




# Имя модуля - __name__

# if __name__ == '__main__':
#     print('Эта программа запущена сама по себе')
# else:
#     print('Меня импортировали в другой модуль')
# ______________________________________________________________________




# Создание собственных модулей

# def say_hi():
#     print('Hi, this is mymodule speaking.')
#
# __version__ = '0.1'

# import mymodule
#
# mymodule.say_hi()
# print('Версия', mymodule.__version__)
# ________________________________________________________________________




# Функция dir
#
# import sys
# print(dir(sys))
# ___________________________________________________________________________




# Краткое введение в классы и объекты
#
# shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
#
# print('Я должен сделать', len(shoplist), 'покупки.')
# print('Покупки:', end=' ')
# for item in shoplist:
#     print(item.split(sep=', '), end=' ')
#
# print('\nТакже нужно купить риса.')
# shoplist.append('рис')
# print('Теперь мой список покупок таков:', shoplist)
#
# print('Отсортирую ка я свой список.')
# shoplist.sort()
# print('Отсортированный список выглядит так:', shoplist)
# print('Первое, что мне нужно купить это:', shoplist[0])
# olditem = shoplist[0]
# del shoplist[0]
# print('Я купил:', olditem)
# ____________________________________________________________________________




# Кортежи
#
# zoo = ('питон', 'слон', 'пингвин')
# print('Количество животных в зоопарке -', len(zoo))
#
# new_zoo = ('обезьяна', 'верблюд', zoo)
# print('Количество клеток в зоопарке -', len(new_zoo))
# print('Все животные в новом зоопарке:', new_zoo)
# print('Животные привезенные из старого зоопарка -', new_zoo[2])
# print('Последне животное, привезенное из старого зоопарка -', new_zoo[2][2])
# print('Количество животных в новом зоопарке -', len(new_zoo)-1+len(new_zoo[2]))
# _______________________________________________________________________________




# Словарь
#
# ab = {
#     'Swaroop': 'swaroop@swaroopch.com',
#     'Larry': 'larry@wall.org',
#     'Matsumoto': 'matz@ruby-lang.org',
#     'Spammer': 'spammer@hotmail.com'
# }
#
# print('Адрес Swaroop\'a', ab['Swaroop'])
# del ab['Spammer']
# print('\nВ адресной книге {} контакта\n'.format(len(ab)))
# for name, address in ab.items():
#     print('Контакт {} с адресом{}'.format(name, address))
#
# ab['Guido'] = 'guido@gmail.com'
# if 'Guido' in ab:
#     print('\nАдрес Guido:', ab['Guido'])
# __________________________________________________________________________________




# Последовательности
#
# shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
# name = 'swaroop'
#
# операции индексирования
# print('Элемент 0 -', shoplist[0])
# print('Элемент 1 -', shoplist[1])
# print('Элемент 2 -', shoplist[2])
# print('Элемент 3 -', shoplist[3])
# print('Элемент -1 -', shoplist[-1])
# print('Элемент -2 -', shoplist[-2])
# print('Символ 0 -', name[0])
#
# # Срез списка
# print('Элементы с 1 по 3:', shoplist[1:3])
# print('Элементы с 2 до конца:', shoplist[2:])
# print('Элементы с 1 по -1:', shoplist[1:-1])
# print('Элементы от начала до конца', shoplist[:])
#
# # Срез строки
# print('Символ с 1 по 3:', name[1:3])
# print('Символ с 2 до конца:', name[2:])
# print('Символ с 1 по -1:', name[1:-1])
# print('Символ от начала до конца:', name[:])
# ___________________________________________________________________________________




# Множество
#
# bri = set(['Бразилия', 'Россия', 'Индия'])
# 'Индия' in bri
# 'США' in bri
#
# bric = bri.copy()
# bric.add('Китай')
# bric.issuperset(bri)
# bri.remove('Россия')
# bri & bric
# print(bri)
# ________________________________________________________________




# Ссылки

# print('Простое присваивание')
# shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

# mylist = shoplist
# del shoplist[0]

# print('shoplist:', shoplist)
# print('mylist:', mylist)

# print('Копирование при помощи полного среза')
# mylist = shoplist[:]

# del mylist[0]

# print('shoplist:', shoplist)
# print('mylist:', mylist)
# ___________________________________________________________________




# Строки
#
# name = 'Swaroop'
#
# if name.startswith('Swa'):
#     print('Да, строка начинается на "Swa"')
# if 'a' in name:
#     print('Да, она содержит строку "a"')
# if name.find('war'):
#     print('Да, она содержит строку "war"')
#
# delimiter = '_*_'
#
# my_list = ['Бразилия', 'Россия', 'Индия', 'Китай']
# print(delimiter.join(my_list))
# ___________________________________________________________________________
