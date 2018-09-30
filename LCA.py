#Node object for our binary tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Checks if data is in given tree
def contains(cur, node):
    if cur.data == node:
        return True
    A = B = False
    if cur.left != None:
        A = contains(cur.left, node)
    if cur.right != None:
        B = contains(cur.right, node)
    return A or B

def LCA(cur, n1, n2):
    if (n1 == n2):
        return n1
    #if n1 and n2 are in root.left
    if (contains(cur.left, n1) and contains(cur.left, n2)):
        return LCA(cur.left, n1, n2)
    #if n1 and n2 are in root.right
    elif (contains(cur.right, n1) and contains(cur.right, n2)):
        return LCA(cur.right, n1, n2)
    #if n1 and n2 are in root only
    if (contains(root, n1) and contains(cur, n2)):
        return cur.data
    #Any other case
    return None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

node1 = 5 ; node2 = 6
print("The lowest common ancestor of {} and {} is {}".format(node1,node2,LCA(root, node1, node2)))
