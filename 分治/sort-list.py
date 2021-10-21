class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # inplaced, O(n*logn) -> quickSort and mergeSort
        # mergeSort
        # end point
        if not head or not head.next:
            return head
        # saparate into two parts
        mid_node = self.midNode(head)
        right = mid_node.next
        mid_node.next = None
        left = head

        # recursive sort left and  right
        left = self.sortList(left)
        right = self.sortList(right)
        # after sorted, we merge them
        return self.mergeSort(left, right)
    
    def midNode(self, head):
        if not head or not head.next:
            return head
        
        slow = head
        quick = head.next.next
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
        
        return slow
    
    def mergeSort(self, left, right):
        fake_head = ListNode(-1)
        cur = fake_head
        while left and right:
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next
        
        if left:
            cur.next = left
        else:
            # right
            cur.next = right
        return fake_head.next