# 11. タブをスペースに置換
# with open('popular-names.txt') as data_file:
#     for line in data_file:
#         print(line.replace('\t', ' '), end = '')

import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
df.to_csv('popular-names-spaces.txt', sep=' ', header=None, index=None)



## Unix command
# sed ‘s/regexp/replacement/flags’
# For example here will be sed 's/\t/ /g'

# tr a b < file
# For example here will be tr '\t' ' ' < hightemp.txt

# expand t 1 hightemp.ext