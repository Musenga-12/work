def strings_to_length_dict(strings):
    length_dict={}
    for string in strings:
        length_dict[string]=len(string)
    return length_dict
strings=["apple","banana","cherry"]
result=strings_to_length_dict(strings)
print(result)