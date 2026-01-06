# Omer Subasi 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def isPalindrome(head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        l, r = 0, len(arr) - 1   
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
            
        return True
