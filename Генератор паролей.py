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


count_pas = int(input('Укажите желаемое количество паролей для генерации: \n'))
len_pas = int(input('Укажите требуемую длинну паролей для генерации: \n'))
need_dig = input('Использовать цифры? (Да/Нет): \n')
need_up_let = input('Использовать заглавные буквы? (Да/Нет): \n')
need_low_let = input('Использовать строчные буквы? (Да/Нет): \n')
need_sym = input('Использовать символы? (Да/Нет): \n')
need_difsym = input('Исключать ли неоднозначные символы il1Lo0O? (Да/Нет): \n')


if need_dig == 'Да':
    chars += digits
if need_up_let == 'Да':
    chars += uppercase_letters
if need_low_let == 'Да':
    chars += lowercase_letters
if need_sym == 'Да':
    chars += punctuation
if need_difsym == 'Да':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')



def generate_password(length, chars):
    li_pas = []
    for i in range(count_pas):
        for _ in range(length):
            li_pas[i] += choice(chars)

    return li_pas


print(generate_password(len_pas, chars))