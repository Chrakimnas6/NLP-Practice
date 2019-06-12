from functools import reduce

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



