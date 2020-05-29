## 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# with open('popular-names.txt') as data_file, open('col1.txt', mode='w') as col1_file, open('col2.txt', mode='w') as col2_file:
#     for line in data_file:
#         cols = line.split('\t')
#         col1_file.write(cols[0] + '\n')
#         col2_file.write(cols[1] + '\n')

import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
# : is to select the entire axis
df.iloc[:,0].to_csv('col1.txt', sep=' ', index=False, header=False)
df.iloc[:,1].to_csv('col2.txt', sep=' ', index=False, header=False)


# Unix command
# For compare, cut -f 1 hightemp.txt > col1_test.txt
# diff --report-identical-files col1.txt col1_test.txt