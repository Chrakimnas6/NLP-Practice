## 14.先頭からN行を出力
# n = int(input('N is '))

# with open('hightemp.txt') as data_file:
#     for i, line in enumerate(data_file):
#         if i >= n:
#             break
#         print(line.rstrip()

import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
print(df.head(5).to_string(index=False, header=False))


# Unix command is in 14_test.sh