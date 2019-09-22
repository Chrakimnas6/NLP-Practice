cut -f 1 hightemp.txt | sort | uniq > 17_test.txt

python3 17.py | sort > 17_test_2.txt

diff --report-identical-files 17_test.txt 17_test_2.txt