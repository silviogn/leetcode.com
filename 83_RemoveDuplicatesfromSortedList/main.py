'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def deleteDuplicates(self, head):

        if head is None:
            return None

        element = head.next
        return_element = ListNode(head.val, None)
        last_element = return_element
        dict_elements = {return_element.val: return_element.val}

        while element is not None:
            if element.val not in dict_elements:
                dict_elements[element.val] = element.val
                last_element.next = ListNode(element.val)
                last_element = last_element.next

            element = element.next
        return return_element
