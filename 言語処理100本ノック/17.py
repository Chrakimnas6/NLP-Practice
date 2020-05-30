## 17. １列目の文字列の異なり

# with open('hightemp.txt') as data_file:
#     my_set = set()
#     for line in data_file:
#         words = line.split('\t')
#         my_set.add(words[0])

# for n in my_set:
#     print(n)
import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
names = df[0].unique()
names.sort()
print(names)