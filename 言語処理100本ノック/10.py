## 10.　行数のカウント
count = 0
with open('hightemp.txt') as data_file:
    for line in data_file:
        count += 1

print(count)

# Unix command 
# wc -l 
# wc -c 総バイト数
# wc -w 単語数