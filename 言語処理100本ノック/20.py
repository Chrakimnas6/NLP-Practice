# 20. JSONデータの読み込み

# import json

# with open('jawiki-country.json') as data_file:
#     for line in data_file:
#         data_jason = json.loads(line)
#         if data_jason['title'] == 'イギリス':
#             print(data_jason['text'])

import pandas as pd
wiki = pd.read_json('jawiki-country.json', lines=True)
print(wiki[wiki['title'] == 'イギリス'].text.values)

