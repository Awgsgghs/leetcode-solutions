"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            newnode = Node(curr.val)
            newnode.next = curr.next
            curr.next = newnode
            curr = newnode.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        oldhead = head
        oldcurr = head
        newhead = head.next
        newcurr = newhead
        while oldcurr:
            oldcurr.next = oldcurr.next.next
            newcurr.next = newcurr.next.next if newcurr.next else None
            oldcurr = oldcurr.next
            newcurr = newcurr.next
        return newhead


