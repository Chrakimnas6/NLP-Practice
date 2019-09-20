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