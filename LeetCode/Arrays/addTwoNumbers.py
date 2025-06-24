class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        targetNode = ListNode()
        current = targetNode
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.value if l1 else 0
            val2 = l2.value if l2 else 0
            total = val1 + val2 + carry
            # Calculate the new digit
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return targetNode.next


# converts an array into a reversed linked list
def arrayToLinkList(array):
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for value in array[1:]:
        current.next = ListNode(value)
        current = current.next
    # Returns Node object or None if tail
    return head


def main():
    # Convert arrays to linked lists
    l1, l2 = [2, 4, 3], [5, 6, 4]
    l1Head = arrayToLinkList(l1)
    l2Head = arrayToLinkList(l2)
    # printList(l1List.head)
    solution = Solution()
    print(solution.addTwoNumbers(l1Head, l2Head))
    printList(solution.addTwoNumbers(l1Head, l2Head))


def printList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print()


if __name__ == "__main__":
    main()