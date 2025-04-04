#!/usr/bin/python3
import sys

append_write = __import__('2-append_write').append_write

nb_characters_added = append_write(sys.argv[1], sys.argv[2] + "\n")
print(nb_characters_added)
