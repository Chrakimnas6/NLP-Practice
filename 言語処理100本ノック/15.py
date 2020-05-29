## 15. 末尾のN行を出力
import sys, pandas as pd
n = int(input('N is: '))

if (n < 0):
    sys.exit('fuck u give me a positive number')

df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
print(df.tail(n).to_string(index=False, header=False))

