## 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

from itertools import groupby

cities = []
with open('hightemp.txt') as data_file:
    for line in data_file:
        cities.append(line.split('\t')[0])

cities.sort()
result = [(city, len(list(group))) for city, group in groupby(cities)]

result.sort(key = lambda city: city[1], reverse = True)

for city in result:
    print('{city}({count})'.format(city=city[0], count=city[1]))