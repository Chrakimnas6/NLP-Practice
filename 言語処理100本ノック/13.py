## 13. col1.txtとcol2.txtをマージ

# with open('col1.txt') as col1_file, open('col2.txt') as col2_file, open('merge.txt', mode='w') as write_file:
#     for col1_line, col2_line in zip(col1_file, col2_file):
#         write_file.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')
import pandas as pd
df1 = pd.read_csv('col1.txt', header=None)
df2 = pd.read_csv('col2.txt', header=None)
# the axis to concatenate along, default is 0, which is the index
df = pd.concat([df1, df2], axis=1)
df.to_csv('merge.txt', sep='\t', header=False, index=False)


# Unix command
# paste col1.txt col2.txt > merge_test.txt
# and use diff