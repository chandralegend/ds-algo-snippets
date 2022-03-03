class Node:
    left = None
    right = None
    val = None

    def __init__(self, val):
        self.val = val


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    inorder(root.left)
    inorder(root.right)
    print(root.val, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)
print("\nPreorder traversal ")
preorder(root)
print("\nPostorder traversal ")
postorder(root)
