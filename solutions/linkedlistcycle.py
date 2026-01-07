# Omer Subasi

class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def linkedListCycle(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
         
    return False
