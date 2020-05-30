## 16. ファイルをN分割する

import math, pandas as pd

N = int(input('N is: '))


# with open('hightemp.txt') as data_file:
#     lines = data_file.readlines()

# file_len = len(lines)
# unit = math.ceil(file_len / n) #how many lines in one file

# # i is from 1, offset is from 0, and then offset + unit
# for i, offset in enumerate(range(0, file_len, unit), 1):
#     with open('ht_{:02d}.txt'.format(i), mode = 'w') as out_file:
#         for line in lines[offset:offset + unit]:
#             out_file.write(line)

df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
unit = math.ceil(len(df) / N)
for n in range(N):
    df_split = df.iloc[n * unit : (n + 1) * unit]
    df_split.to_csv('popular-names' + str(n) + '.txt', sep='\t', header=False, index=False)