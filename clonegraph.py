# Omer Subasi

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def performClone(node, clone_map = {}):
    if node in clone_map:
        return clone_map[node]
    
    newNode = Node(node.val)
    clone_map[node] = newNode

    for neighbor in node.neighbors:
        cloned_neighbor = self.performClone(neighbor, clone_map)
        newNode.neighbors.append(cloned_neighbor)
    return newNode

def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None
    return self.performClone(node)
