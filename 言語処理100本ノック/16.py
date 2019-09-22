## 16. ファイルをN分割する

import math

n = int(input('N is: '))

with open('hightemp.txt') as data_file:
    lines = data_file.readlines()

file_len = len(lines)
unit = math.ceil(file_len / n) #how many lines in one file

# i is from 1, offset is from 0, and then offset + unit
for i, offset in enumerate(range(0, file_len, unit), 1):
    with open('ht_{:02d}.txt'.format(i), mode = 'w') as out_file:
        for line in lines[offset:offset + unit]:
            out_file.write(line)