# --key =3,3 means the starting field position and the ending field position
# are both 3
# -n is --numeric-sort, -r is --reverse
sort popular-names.txt -k 3,3 -n -r > 18_test.txt


python3 18.py > 18_test_2.txt

diff -s 18_test.txt 18_test_2.txt