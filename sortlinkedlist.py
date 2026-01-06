# Omer Subasi

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(list1, list2):
        h1, h2 = list1, list2
        curr = dummy = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next
        curr.next = h1 or h2
        return dummy.next

    def splitList(head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        return second_head

    def sortList(head):
        if not head or not head.next:
            return head
        second_head = self.splitList(head)
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(second_head)
        return self.mergeTwoLists(left_sorted, right_sorted)


