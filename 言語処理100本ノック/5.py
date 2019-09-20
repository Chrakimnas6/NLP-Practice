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