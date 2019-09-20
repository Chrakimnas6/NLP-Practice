## 14.先頭からN行を出力
n = int(input('N is '))

with open('hightemp.txt') as data_file:
    for i, line in enumerate(data_file):
        if i >= n:
            break
        print(line.rstrip())


# Unix command is in 14_test.sh