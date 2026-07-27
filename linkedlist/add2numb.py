class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        catch = 0
        while l1 or l2 or catch:
            total = catch
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            catch = total // 10
            res.next = ListNode(total % 10)
            res = res.next
        return head.next
