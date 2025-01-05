L = [11,22,"helllo", "hi",[11,44]]
lst = []
for el in L:
    print(el)
    if type(el) == list:
        for i in el:
            print(i)
            if type(el) == str:
                lst.append(i)
    else:
        if type(el) == str:
            lst.append(el)

print(lst)