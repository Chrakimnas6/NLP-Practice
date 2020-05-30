## 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

# from itertools import groupby

# cities = []
# with open('hightemp.txt') as data_file:
#     for line in data_file:
#         cities.append(line.split('\t')[0])

# cities.sort()
# result = [(city, len(list(group))) for city, group in groupby(cities)]

# result.sort(key = lambda city: city[1], reverse = True)

# for city in result:
#     print('{city}({count})'.format(city=city[0], count=city[1]))

import pandas as pd

df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
vc = df[0].value_counts()

df_1 = pd.DataFrame(vc)
print(df_1)
df_1 = df_1.reset_index()
print(df_1)
df_1.columns = ['name', 'count']
# so when two counts are the same, we sort name by descending
print(df_1.sort_values(['count', 'name'], ascending=[False, False]))