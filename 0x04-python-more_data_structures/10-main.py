#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John':12, 'Mike':13, 'Sue':16, 'Sally':15}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))
