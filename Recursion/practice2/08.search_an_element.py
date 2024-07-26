def search_elment(x,L):
    if len(L)==0:
        return False
    if x==L[0]:
        return True
    return search_elment(x,L[1:])

print(search_elment(100,[11,10,12,23]))