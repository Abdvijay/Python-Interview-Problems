edges = {}
while True:
    edge = input("Enter the edge and weight separated by comma (ex. ab,3) (Note : Enter Done to exit): ").split(",")

    if len(edge) < 2 and edge[0].lower() != 'done': # Checking len of edge (ex. ab alone) except done
        print("Please enter edge as well as weight :)")
        continue

    if len(edge) == 1 and edge[0].lower() == 'done': # Checking len of edge is 1 and edge is done then stop the getting edges from user
        break

    if edge[0] not in edges: # Checking the entered edge already satisfied or not
        edges[edge[0]] = edge[1]
    else:
        edges[edge[0]] += edge[1]

combinations = {}

def find_paths(start_edge,current_path,total_weight):
    last_node = start_edge[-1] # Getting starting edge last node which is (ex. ab -> b)
    extended = False # Defaultly extended False

    for edge,weight in edges.items():
        if edge[0] == last_node and edge not in current_path: # Checking edge first node with last node and also the edge not in current path
            find_paths(edge,current_path + [edge],int(total_weight) + int(weight))
            extended = True # Change the flag because the above condition says the current edge has continuity
    
    if not extended: # Once the extended is done then execute this statement
        full_path = "->".join(e[0] for e in current_path) + "->" + current_path[-1][1] # 1st part -> current path 1st letter [ex. ab,bc,cd], 2nd path is last path 1st index pos character
        combinations[full_path] = int(total_weight) # Adding weightages

# Generate all possible continuous paths
for edge,weight in edges.items():
    find_paths(edge,[edge],weight)

start_node = input("Enter the starting edge : ").lower()[0] # Getting staring edge as lower input
end_node = input("Enter the ending edge : ").lower()[0] # Getting ending edge as lower input

final_edges = {}
for edge,weight in combinations.items():
    if edge[0] == start_node and edge[-1] == end_node and edge not in final_edges: # Checking first node and end node with every combinations paths
        final_edges[edge] = int(weight)

if len(final_edges) == 0: # Checking the empty egdes
    print(f'No valid edges found from {start_node} -> {end_node}')
else:
    min_value = min(final_edges.values()) # Finding min weights among all the final paths
    min_path = [edge for edge,weight in final_edges.items() if weight == min_value] # Finding corresponded min values related paths
    print(f"The minimalistic edge is {min_path} and weight is {min_value}")

# Output

# Enter the edge and weight separated by comma (ex. ab,3) (Note : Enter Done to exit): ab,1
# Enter the edge and weight separated by comma (ex. ab,3) (Note : Enter Done to exit): bc,2
# Enter the edge and weight separated by comma (ex. ab,3) (Note : Enter Done to exit): cd,1
# Enter the edge and weight separated by comma (ex. ab,3) (Note : Enter Done to exit): ad,4
# Enter the edge and weight separated by comma (ex. ab,3) (Note : Enter Done to exit): bd,3
# Enter the edge and weight separated by comma (ex. ab,3) (Note : Enter Done to exit): done
# Enter the starting edge : a
# Enter the ending edge : d
# The minimalistic edge is ['a->b->c->d', 'a->b->d', 'a->d'] and weight is 4