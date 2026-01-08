# Omer Subasi

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeKthEndOfList(head, k):
    dummy = ListNode(0)
    dummy.next = head
    explorer = dummy
    spotter = dummy
    for _ in range(k):
        explorer = explorer.next
        if not explorer:
            return head
    
    while explorer.next:
        explorer = explorer.next
        spotter = spotter.next
    
    spotter.next = spotter.next.next
    return dummy.next
