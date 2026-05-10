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
        if head is not None:
            newHead = Node(head.val)
        else:
            newHead = None
        retNewHead = newHead
        oldHead = head
        copyHash = {}
        while head != None:
            
            if head.next != None:
                newHead.next = Node(head.next.val)
            copyHash[head] = newHead
            head = head.next
            newHead = newHead.next
        newHead = retNewHead
        head = oldHead
        while newHead != None:
            randomNode = head.random
            if randomNode is not None:
                newHead.random = copyHash[randomNode]
            else:
                newHead.random = None
            head = head.next
            newHead = newHead.next
        
        return retNewHead


        