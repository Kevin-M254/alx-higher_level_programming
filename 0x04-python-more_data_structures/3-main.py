#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = {'Java', 'C', 'Python'}
set_2 = {'Ruby', 'Perl', 'C'}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
