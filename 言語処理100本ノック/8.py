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