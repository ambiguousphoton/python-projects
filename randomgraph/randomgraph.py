""" THIS MODULE IS FOR GENRATING RANDOM GRAPHS FOR TESTING """

import random 
  
# FOR GENRATING SET OF GRAPHS:
#     For eg: 
#            input: 6, 2
#            output: {0: [0, 1], 1: [1, 2], 2: [2], 3: [3], 4: [4, 2], 5: [5]} 
def genrate_graphset(no_of_nodes: int, maxedges: int) -> dict:
    graph = dict()
    for node in range(no_of_nodes):
        graph[node] = [node]
        neighbours = {node}
        for _ in range(random.randint(0, maxedges)):
            neighbour = random.randint(0, maxedges)
            if neighbour not in neighbours:
                graph[node].append(neighbour)
                neighbours.add(neighbour)

    return graph

# FOR GENRATING ADJECENCY TREE :
#    'roots' input requires a list of nodes which could be manual or genrated random nodes.
#     eg input: (a) [a,b,c,d,e,f] or (b) [1,2,3,4,5]    
#     eg output: {'a': ['a', 'b', 'c'], 'b': ['b', 'd', 'e'], 'c': ['c', 'f'], 'd': ['d'], 'e': ['e'], 'f': ['f']} for (a)
#     Random Nodes can also be genrated by using genrate_random_nodes()
def genrate_adjtree(roots: list) -> dict:
    tree = dict()
    root_pointer = 0
    cp1, cp2 = root_pointer + 1, root_pointer + 2 # child pointer 1 and 2      
    while root_pointer < len(roots):
        tree[roots[root_pointer]] = [roots[root_pointer]]
        if cp1 < len(roots):
            tree[roots[root_pointer]].append(roots[cp1])
        if cp2 < len(roots):
            tree[roots[root_pointer]].append(roots[cp2])
        root_pointer += 1
        cp1 += 2
        cp2 += 2

    return tree

# FOR MAKING RANDOM NODES:
#     Input 'size' as the no. of nodes required for result
#     Outputs a random array of size -> 'size'
#     For eg:
#             input : 6 
#             output : ['P7', 'Y9', 'd1', 'l6', 's7', 'A7']
def genrate_random_nodes(size: int) -> list[str]:
    choices_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    choices_no = '0123456789'
    states = set()
    random_nodes_set = []

    def genrate_states(random_nodes, size):
        n1 = random.randint(0, len(choices_char) - 1) # index 1 for node from choices
        n2 = random.randint(0, len(choices_no) - 1) # index 2 for node from choices
        new_state = choices_char[n1] + choices_no[n2]
        if new_state not in states:
            states.add(new_state)
            random_nodes.append(new_state)
        if len(random_nodes) == size:
            return random_nodes_set        

        return genrate_states(random_nodes, size)

    return genrate_states(random_nodes_set, size)
