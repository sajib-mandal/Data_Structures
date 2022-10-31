# 206. Reverse Linked List


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead
        
        
        
        # Recursive: T O(n), M O(n)
        if head == None or head.next == None:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return p
        
        
        
        
        
        # Iterative: T O(n), M O(n)
        prev, curr = None, head
        while curr:
            nextP = curr.next
            curr.next = prev
            prev = curr
            curr = nextP
        return prev
