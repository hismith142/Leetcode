#Problem: given the heads to two sorted linked lists, return the head of a merged linked list

#Initial thoughts: the problem doesn't provide a linked list, so that presents an edge case. A dummy node can get around that though, and dummy.next can be returned instead. At first I had imagined that each 'index' would get compared to one another and then you'd move on, but you want to compare each current value with the other list's current value, even if they're 'off'. Adding the nodes will be simple; update the tail each time.

#Possible issues: one list may not be empty by the time another one is, so a check will have to be performed that would append the rest of the remaining nodes onto the return pointer.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode() #Making dummy node
        tail = dummy

        while list1 and list2: #If there are values in both lists
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #Updating tail each iteration
        
        tail.next = list1 or list2 #Appending remaining values
        
        return dummy.next