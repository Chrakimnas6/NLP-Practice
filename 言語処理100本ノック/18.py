## 18. 各行を3コラム目の数値の降順にソート

# lines = open('popular-names.txt').readlines()
# lines.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)

# for line in lines:
#     print(line, end='')

import pandas as pd
# add names and sort by name
df = pd.read_csv('popular-names.txt', delimiter="\t", header=None, names=['name', 'sex', 'number', 'year'])
df = df.sort_values(by='number', ascending=False)

print(df)