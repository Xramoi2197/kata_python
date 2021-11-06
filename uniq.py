lst = [
    {"a": 5, "b": 6},
    {"a": 6, "b": 6},
    {"a": 7, "b": 6},
    {"a": 8, "b": 5},
    {"a": 5, "b": 6},
    {"a": 6, "b": 6},
    {"a": 2, "b": 6},
    {"a": 5, "b": 6},
    {"a": 7, "b": 6},
    {"b":7}
]

def uniq(lst, key):
    return set([mp[key] for mp in lst if key in mp.keys()])


print(uniq(lst, "a"))
print(uniq(lst, "b"))