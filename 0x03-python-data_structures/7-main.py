#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (88, 1)
tuple_b = (11, 89)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
