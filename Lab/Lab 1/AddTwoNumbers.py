# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    dummy_head = ListNode(0)
    current = dummy_head

    while l1 or l2 or carry:
        # Get values from the nodes or 0 if the node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        new_digit = total % 10

        # Create a new node with the new digit and move the pointer
        current.next = ListNode(new_digit)
        current = current.next

        # Move to the next nodes in l1 and l2 if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# Helper functions to convert between lists and linked lists
def list_to_linkedlist(lst):
    dummy_head = ListNode(0)
    current = dummy_head
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy_head.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

l1 = list_to_linkedlist([9,9,9,9,9,9,9])
l2 = list_to_linkedlist([9,9,9,9])
result = addTwoNumbers(l1, l2)
print(linkedlist_to_list(result))