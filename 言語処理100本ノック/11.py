# 11. タブをスペースに置換
with open('hightemp.txt') as data_file:
    for line in data_file:
        print(line.replace('\t', ' '), end = '')

## Unix command
# sed ‘s/regexp/replacement/flags’
# For example here will be sed 's/\t/ /g'

# tr a b < file
# For example here will be tr '\t' ' ' < hightemp.txt

# expand t 1 hightemp.ext