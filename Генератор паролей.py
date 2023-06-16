'''
Описание проекта:
программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.
'''
from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


count_pas = input('Укажите желаемое количество паролей для генерации: \n')
len_pas = input('Укажите требуемую длинну паролей для генерации: \n')
need_dig = input('Использовать цифры? (Да/Нет): \n')
need_up_let = input('Использовать заглавные буквы? (Да/Нет): \n')
need_low_let = input('Использовать строчные буквы? (Да/Нет): \n')
need_sym = input('Использовать символы? (Да/Нет): \n')
need_difsym = input('Исключать ли неоднозначные символы il1Lo0O? (Да/Нет): \n')