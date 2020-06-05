# 21. カテゴリ名を含む行を抽出
import pandas as pd
import re
pattern = re.compile('Category')
wiki = pd.read_json('jawiki-country.json', lines = True)
# print(wiki.head())
# DataFrame -> Series -> ndarray
# Series is the data structure for a single column of a DataFrame
# uk = wiki[wiki['title'] == 'イギリス'].text.array
uk = wiki[wiki['title'] == 'イギリス'].to_numpy()[0]
# print(uk[0][0])
lines = uk[0].split('\n')
for l in lines:
    if re.search(pattern, l):
        print(l)