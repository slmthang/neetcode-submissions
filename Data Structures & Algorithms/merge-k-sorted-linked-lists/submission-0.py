# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:

            return None

        for i in range(1, len(lists)):

            head = self.mergeTwoLists(lists[i-1], lists[i])

            lists[i] = head

        return lists[len(lists)-1]
        
    
    def mergeTwoLists(self, a1, a2):

        head = None
        curNode = None

        while(a1 and a2):

            if (a1.val > a2.val):

                if (not head):

                    head = a2
                    curNode = head
                
                else:

                    curNode.next = a2
                    curNode = a2
                
                a2 = a2.next
            
            else:

                if (not head):

                    head = a1
                    curNode = head
                
                else:

                    curNode.next = a1
                    curNode = a1

                a1 = a1.next
        
        while(a1):

            curNode.next = a1
            curNode = a1
            a1 = a1.next

        while(a2):

            curNode.next = a2
            curNode = a2
            a2 = a2.next

        return head


                    



        