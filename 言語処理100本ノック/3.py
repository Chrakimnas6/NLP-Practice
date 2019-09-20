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