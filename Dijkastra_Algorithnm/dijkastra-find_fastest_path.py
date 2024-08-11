graph = {'S':{'A':6 , 'B':2 },
         'A':{'E':1},
         'B':{'A':3 , 'E':5 },
         'E': {}
         }
costs = {
        'A':6,
        'B':2,
        'E':float('inf')
}

parent = {
        'A':'S',
        'B':'S',
        'E': None
}

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node,cost in costs.items() :
        #print(cost,lowest_cost)
        if cost < lowest_cost and node not in processed:
            
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost, lowest_cost_node

processed = []
lowest_cost, lowest_cost_node = find_lowest_cost_node(costs)
print("lowest_cost:", lowest_cost, " lowest_cost_node:", lowest_cost_node)
while lowest_cost_node  is not None:
        print("graph[lowest_cost_node].keys():",graph[lowest_cost_node])
        for next_node in graph[lowest_cost_node].keys():
                new_cost = lowest_cost + graph[lowest_cost_node][next_node]
                if costs[next_node] > new_cost:
                        costs[next_node] = new_cost
                        parent[next_node] = lowest_cost_node
        processed.append(lowest_cost_node)
        lowest_cost, lowest_cost_node = find_lowest_cost_node(costs)

        #print("processed:", processed)
print("processed:", processed)
print("costs:", costs)
print("parent:", parent)

