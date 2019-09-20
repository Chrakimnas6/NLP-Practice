## 15. 末尾のN行を出力
import sys
n = int(input('N is: '))

if (n < 0):
    sys.exit('fuck u give me a positive number')

with open('hightemp.txt') as file_data:
    lines = file_data.readlines()

for line in lines[-n:]:
    print(line.rstrip())

