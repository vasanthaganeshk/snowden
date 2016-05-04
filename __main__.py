from sys import argv
from karp_rabin import find_first

# while running this program run it as $python3 driver.py /path/to/file StringToBeSearched
# Line numbers are not working

_, target, find_str = argv
target_str = open(target).read()

pos = (find_first(target_str, find_str))
for i in pos:
    print target_str[i-5:i], "\033[1;31m{}\033[0m".format(find_str), target_str[i+len(find_str): i+len(find_str) + 5]
