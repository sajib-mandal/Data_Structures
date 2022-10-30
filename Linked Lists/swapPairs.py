def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Write Code
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy
        while head and head.next:
            first_node = head
            second_node = head.next
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            prev_node = first_node
            head = prev_node.next
        return dummy.next
    
        
        # Wrong Code just 1 line up and down
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy
        while head and head.next:
            first_node = head
            second_node = head.next
            prev_node.next = second_node
            second_node.next = first_node
            first_node.next = second_node.next
            prev_node = first_node
            head = prev_node.next
        return dummy.next
