# Omer Subasi

def postorder(root):
    if not root:
        return []
    res = []
    l = postorder(root.left)
    r = postorder(root.right)
    if l:
        for x in l:
            res.append(x)
    if r:
        for x in r:
            res.append(x)
    
    res.append(root.val)
    return res
