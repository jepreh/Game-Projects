"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains as ingle digit.
Add the two numbers and return the sun as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself. 
As python does not have built-in linked list type, we need to create a custom class.
"""

# Each node stores data and a reference to the next node
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next


# Manages the head node and provides methods for common operations
class Linkedlist:
    def __init__(self):
        self.head = None

    # Traverse and print all elements in the linked list
    def printList(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print()


class Solution(object):
    # The main function of the task
    def addTwoNumbers(self, l1, l2):
        length1, length2 = len(l1), len(l2)
        l1List, l2List = Linkedlist(), Linkedlist()
        l1Head = self.arrayToLinkList(l1)
        l1List.head = l1Head
        l2Head = self.arrayToLinkList(l2)
        l2List.head = l2Head

        sum1 = self.sumLinkList(l1Head, length1)
        sum2 = self.sumLinkList(l2Head, length2)
        total = sum1 + sum2

        total = self.intToLinkList(total)

        return total

    # Traverse through the linked list, from the head
    def sumLinkList(self, head, length):
        sum = 0
        magnitude = 1 * pow(10, length-1)
        current = head
        while current:
            sum = sum + current.value * magnitude
            current = current.next
            magnitude = magnitude // 10
        return sum

    # converts an array into a reversed linked list
    def arrayToLinkList(self, array):
        if not array:
            return None
        head = None
        for value in array:
            newNode = Node(value)
            newNode.next = head
            head = newNode
        # Returns Node object or None if tail
        return head

    def intToLinkList(self, total: int):
        totalStr = str(total)
        head = None
        tail = None
        for value in totalStr:
            newNode = Node(int(value))
            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        return head
    
def main():
    l1, l2 = [2, 4, 3], [5, 6, 4]
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))


if __name__ == "__main__":
    main()