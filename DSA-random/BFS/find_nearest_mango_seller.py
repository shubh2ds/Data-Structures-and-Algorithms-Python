graph = {}
graph['you'] = ['alice','bob','clair']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj','peggy']
graph['clair'] = ['thom', 'jonny']

graph['peggy'] = []
graph['anuj'] = []
graph['thom'] = []
graph['jonny'] = []

from collections import deque
def person_is_seller(name):
    return name[-1] == 'm'

def search_nearest(name):
    search_queue = deque()
    #search_queue = search_queue + graph[name]
    search_queue.extend(graph[name])

    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("nearest mango seller:",person)
                return True
            else:
                #search_queue  = search_queue + graph[person]
                search_queue.extend(graph[person])
                searched.append(person)
    return False

print(search_nearest('you'))

#nearest mango seller: thom
#True
