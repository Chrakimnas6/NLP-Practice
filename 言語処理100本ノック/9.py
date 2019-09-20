import random
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