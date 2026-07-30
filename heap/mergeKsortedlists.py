class Solution:
    def merge2lists(self,list1,list2):
        curr=ListNode()
        head=curr
        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        curr.next=list1 if list1 else list2
        return head.next
    def mergeKlistshelp(self,lists,start,end):
        if start==end:
            return lists[start]
        if start==end-1:
            return self.merge2lists(lists[0],lists[1])
        mid=(start+end)//2
        leftlist=self.mergeKlistshelp(lists,start,mid)
        rightlist=self.mergeKlistshelp(lists,mid+1,end)
        return self.merge2lists(leftlist,rightlist)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        return self.mergeKlistshelp(lists,0,len(lists)-1)