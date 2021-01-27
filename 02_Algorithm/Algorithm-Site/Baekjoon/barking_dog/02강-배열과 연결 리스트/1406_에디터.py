import sys

input = lambda : sys.stdin.readline().strip()


class Node:
    def __init__(self, alpha):
        self.alpha = alpha
        self.pre = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node('head')

    def left(self, node):
        if node == self.head:
            return node
        return node.pre

    def right(self, node):
        if not node.next:
            return node
        return node.next

    def pop(self, node):
        if node == self.head:
            return node
        pre_node = node.pre
        next_node = node.next
        pre_node.next = next_node
        if next_node:
            next_node.pre = pre_node
        return pre_node

    def append(self, cur_node, node):
        next_node = cur_node.next
        cur_node.next = node
        node.pre = cur_node
        if next_node:
            next_node.pre = node
        node.next = next_node
        return node

    def print_all(self):
        node = self.head.next
        while node:
            print(node.alpha, end='')
            node = node.next
        return



S = list(input())
M = int(input())
linked_list = LinkedList()
pre_node = linked_list.head

for idx in range(len(S)):
    node = Node(S[idx])
    linked_list.append(pre_node, node)
    pre_node = node

for _ in range(M):
    command = input()
    if command == 'L':
        node = linked_list.left(node)
    elif command == 'D':
        node = linked_list.right(node)
    elif command == 'B':
        node = linked_list.pop(node)
    else:
        new_node = Node(command[-1])
        node = linked_list.append(node, new_node)

linked_list.print_all()