
def DLS(tree, node, depth, limit, visited):
    if node is None:
        return

    visited.append(node)

    if depth == limit:
        return

    for child in tree.get(node, []):
        DLS(tree, child, depth + 1, limit, visited)


n = int(input("Enter number of nodes: "))

tree = {}

print("Enter node and children of each node (space-separated):")

for i in range(n):
    node = int(input("Enter node: "))
    children = list(map(int, input(f"Enter children of node {node}: ").split()))
    tree[node] = children

root = int(input("Enter root node: "))
limit = int(input("Enter depth limit: "))

visited = []
DLS(tree, root, 0, limit, visited)

print("Nodes visited using DLS:", visited)