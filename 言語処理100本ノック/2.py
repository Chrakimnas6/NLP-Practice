## 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
str1 = 'パトカー'
str2 = 'タクシー'

## method 1
# result = ''
# for (w1, w2) in zip(str1, str2):
#     result += w1 + w2

## method 2
## result = ''.join(reduce(lambda x, y: x + y, zip(str1, str2)))
result = str1 + str2
print('02.「パトカー」＋「タクシー」＝「パタトクカシーー」')
print(result)