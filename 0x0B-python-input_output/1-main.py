#!/usr/bin/python3

import sys
write_file = __import__('1-write_file').write_file

nb_characters = write_file(sys.argv[1], sys.argv[2] + "\n")
print(nb_characters)
