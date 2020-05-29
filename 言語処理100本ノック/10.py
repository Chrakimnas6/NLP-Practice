## 10.　行数のカウント update
import pandas as pd
count = 0
with open('popular-names.txt') as data_file:
    for line in data_file:
        count += 1

df = pd.read_csv('popular-names.txt', header=None)
print(len(df))

# Unix command 
# wc -l 
# wc -c 総バイト数
# wc -w 単語数