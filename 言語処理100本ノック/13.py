## 13. col1.txtとcol2.txtをマージ

with open('col1.txt') as col1_file, open('col2.txt') as col2_file, open('merge.txt', mode='w') as write_file:
    for col1_line, col2_line in zip(col1_file, col2_file):
        write_file.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')

# Unix command
# paste col1.txt col2.txt > merge_test.txt
# and use diff