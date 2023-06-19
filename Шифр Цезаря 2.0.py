


n = input()

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''
result = ''
m = n
for i in ['.', ',', '-', '!', '?', '"']:
    m = m.replace(i, '')


len_li = m.split()

for j in len_li:
    for el in j:
        if el in eng_lower_alphabet:
            cur_n = ord("a") + (ord(el) - ord("a") + 26 + len(j)) % 26
            answer += chr(cur_n)
        elif el in eng_upper_alphabet:
            cur_n = ord("A") + (ord(el) - ord("A") + 26 + len(j)) % 26
            answer += chr(cur_n)
        elif el == ' ':
            print()
            answer += el

        else:
            answer += el
k = 0
for c in n:
    if c.isalpha():
        result += answer[k]
        k += 1
    else:
        result += c

print(result)