class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head
        for i in range(k):
            if not tail:
                return head
            tail = tail.next
        newhead = self.reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)
        return newhead

    def reverse(self, curr, end):
        prev = None
        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev