from functools import reduce
import random

## 00. 文字列の逆順
target = 'stressed'
result = target[::-1]
print('00. 文字列の逆順')
print(result)

## 01. 「パタトクカシーー」
target = 'パタトクカシ'
result = target[::2]
print('01. 「パタトクカシーー」')
print(result)

## 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
str1 = 'パトカー'
str2 = 'タクシー'

## method 1
# result = ''
# for (w1, w2) in zip(str1, str2):
#     result += w1 + w2

## method 2
result = ''.join(reduce(lambda x, y: x + y, zip(str1, str2)))
print('02.「パトカー」＋「タクシー」＝「パタトクカシーー」')
print(result)

## 03. 円周率
target = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
result = []
words = target.split()

## method 1
# for word in words:
#     result.append(len(word) - word.count(',') - word.count('.'))

## method 2
for word in words:
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    result.append(count)
print('03. 円周率')
print(result)

## 04. 元素記号
only_first = (1, 5, 6, 7, 8, 9, 15, 16, 19)
target = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
result = {}

words = target.split()
for (index, word) in enumerate(words, 1):
    if index in only_first:
        result[word[0:1]] = index
    else:
        result[word[0:2]] = index

print('04. 元素記号')
print(result) 

## 05. n-gram
def n_gram(target, n):

    result = []
    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])

    return result

target = 'I am an NLPer'
words_target = target.split()

result = n_gram(words_target, 2)

print('05. n-gram')
print(result)

## 06. 集合

print('06. 集合')
set_x = set(n_gram('paraparaparadise', 2))
print('A: ' + str(set_x))

set_y = set(n_gram('paragraph', 2))
print('B: ' + str(set_y))

set_or = set.union(set_x, set_y)
print('和集合: ' + str(set_or))
set_and = set_x & set_y # can also use intersection
print('積集合: ' + str(set_and))
set_minus = set_x - set_y # difference
print('差集合: ' + str(set_minus))

print('se in X? ' + str('se' in set_x))
print('se in Y? ' + str('se' in set_y))

## 07. テンプレートによる文生成
# def templete(x, y, z):
#     return str(x) + '時の' + y + 'は' + str(z)


# result = templete(12, '気温', 22.4)
def templete(x, y ,z):
    return '{}時の{}は{}'.format(x, y, z)

print('07. テンプレートによる文生成')
print(templete(12, '気温', 22.4))

## 08. 暗号文
def cipher(target):
    result = ''
    for x in target:
        if (x.islower()):
            result += chr(219 - ord(x))
        else:
            result += x
    return result

target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
result = cipher(target)
print('08. 暗号文')
print(result)
result2 = cipher(result)
print(result2)

## 09. Typoglycemia
def typoglycemia(target):
    result = []
    for word in target.split():
        if len(word) < 4:
            result.append(word)
        else:
            word_ran = list(word[1:-1]) #convert str to list since random.shuffle needs a list
            random.shuffle(word_ran)
            result.append(word[0] + ''.join(word_ran) + word[-1]) #append a string, take the first and the last alphabet add the shuffled list
    return ' '.join(result) # turn the list to a string

print('09. Typoglycemia')
target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(target))








