#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    elif len(a_dictionary) == 0:
        return None
    else:
        a = []
        for value in a_dictionary.values():
            a.append(value)
        val = a[0]
        for i in range(1, len(a)):
            if a[i] > val:
                val = a[i]
        for key, value in a_dictionary.items():
            if value == val:
                return key
