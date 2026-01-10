# Omer Subasi

def preorder(root):
    if not root:
        return []
    res = [root.val]
    l = preorder(root.left)
    r = preorder(root.right)
    if l:
        for x in l:
            res.append(x)
    if r:
        for x in r:
            res.append(x)

    return res
