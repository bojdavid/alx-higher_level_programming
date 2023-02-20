#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        a = []
        for key, val in a_dictionary.items():
            if val == value:
                a.append(key)
        for i in a:
            a_dictionary.pop(i)
        return a_dictionary
    else:
        return a_dictionary
