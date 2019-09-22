## 18. 各行を3コラム目の数値の降順にソート

lines = open('hightemp.txt').readlines()
lines.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)

for line in lines:
    print(line, end='')