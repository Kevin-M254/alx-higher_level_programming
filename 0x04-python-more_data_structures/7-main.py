#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'Language':"C", 'number':89, 'track':"low level"}
new_dict = update_dictionary(a_dictionary, 'Language',"Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'City',"Nairobi")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
