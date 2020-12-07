def update_dictionary(d,key,value):
    value_s=[value]
    if key in d:
        d[key]+=value_s
    else:
        key_new = key*2
        if key_new in d:
            d[key_new] += value_s
        else:
            d[key_new] =value_s

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}