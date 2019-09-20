## 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
with open('hightemp.txt') as data_file, open('col1.txt', mode='w') as col1_file, open('col2.txt', mode='w') as col2_file:
    for line in data_file:
        cols = line.split('\t')
        col1_file.write(cols[0] + '\n')
        col2_file.write(cols[1] + '\n')

# Unix command
# For compare, cut -f 1 hightemp.txt > col1_test.txt
# diff --report-identical-files col1.txt col1_test.txt