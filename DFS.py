# DFS function
def dfs(node, visited, tree):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for child in tree[node]:
            dfs(child, visited, tree)

# Taking user input
n = int(input("Enter number of nodes: "))

tree = {}

print("Enter node and children of each node (space-separated):")

for i in range(n):
    node = int(input("Enter node: "))
    children = list(map(int, input(f"Enter children of node {node}: ").split()))
    tree[node] = children

root = int(input("Enter root node: "))

# DFS Traversal
visited = set()
print("DFS Traversal:")
dfs(root, visited, tree)