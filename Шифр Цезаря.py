'''
Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:
'''

action = input('Что делаем? (ш = шифрование / д = дешифрование): \n')
lang = input('Язык текста? (ru / en): \n')
step = int(input('Шаг сдвига: \n'))
text = input("Текст: ")
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
answer = ''

if action == 'д' and lang == 'en':
    for el in text:
        if el.isalpha():
            cur_n = ord("a") + (ord(el) - ord("a") + 26 - step) % 26
            answer += chr(cur_n)
        else: answer += el

if action == 'д' and lang == 'ru':
    for el in text:
        cur_n = ord("а") + (ord(el) - ord("а") + 32 - step) % 32
        print(chr(cur_n), end="")


print(answer)