
def DLS(tree, node, depth, limit, visited):
    if node is None:
        return

    visited.append(node)

    if depth == limit:
        return

    for child in tree.get(node, []):
        DLS(tree, child, depth + 1, limit, visited)


def IDDFS(tree, root, max_depth):
    for limit in range(max_depth + 1):
        visited = []
        DLS(tree, root, 0, limit, visited)
        print(f"Depth Limit {limit}: Visited nodes {visited}")

n = int(input("Enter number of nodes: "))

tree = {}

print("Enter node and children of each node (space-separated):")

for i in range(n):
    node = int(input("Enter node: "))
    children = list(map(int, input(f"Enter children of node {node}: ").split()))
    tree[node] = children

root = int(input("Enter root node: "))
max_depth = int(input("Enter maximum depth: "))


IDDFS(tree, root, max_depth)