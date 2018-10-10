# A recursive python program to find LCA of two nodes 
# n1 and n2 
  
# A Binary tree node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Function to find LCA of n1 and n2. The function assumes 
# that both n1 and n2 are present in BST 
def lca(root, n1, n2): 
      
    # Base Case 
    if root is None: 
        return None
  
    # If both n1 and n2 are smaller than root, then LCA 
    # lies in left 
    if(root.data > n1 and root.data > n2): 
        return lca(root.left, n1, n2) 
  
    # If both n1 and n2 are greater than root, then LCA 
    # lies in right  
    if(root.data < n1 and root.data < n2): 
        return lca(root.right, n1, n2) 
  
    return root 
  
# Driver program to test above function 
  
# Let us construct the BST shown in the figure 
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
  
n1 = 10 ; n2 = 14
t = lca(root, n1, n2) 
print "LCA of %d and %d is %d" %(n1, n2, t.data) 
  
n1 = 14 ; n2 = 8
t = lca(root, n1, n2) 
print "LCA of %d and %d is %d" %(n1, n2 , t.data) 
  
n1 = 10 ; n2 = 22
t = lca(root, n1, n2) 
print "LCA of %d and %d is %d" %(n1, n2, t.data) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

#bfs

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
    vertex = queue.pop(0)
    if vertex not in visited:
        visited.add(vertex)
        queue.extend(graph[vertex] - visited)
return visited

# bfs
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None
   


# find path graph
print(find_all_paths(graph, 'A', 'D')) 
print(find_shortest_path(graph, 'A', 'D'))

