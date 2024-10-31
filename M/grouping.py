def group_names_by_age(names_and_ages):
    age_dict={}
    for name,age in names_and_ages:
        if age not in age_dict:
            age_dict[age]=[]
        age_dict[age].append(name)
    return age_dict
names_and_ages=[("Alice",30),("Bob",25),("Charlie",30),("David",25)]
result=group_names_by_age(names_and_ages)
print(result)