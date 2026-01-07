# Omer Subasi

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertBinaryTree(root):
    if not root or (not root.left and not root.right):
        return root
    
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)

    tmp = root.left
    root.left = root.right
    root.right = tmp

    return root
