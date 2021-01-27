import sys


input = lambda : sys.stdin.readline().strip()

class Node:
    def __init__(self, num):
        self.num = num
        self.pre = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def turn_next(self, node, K):
        for k in range(K):
            node = node.next
            if node == self.head:
                node = node.next
        return node

    def append(self, cur_node, num):
        new_node = Node(num)
        cur_node.next = new_node
        new_node.pre = cur_node
        return new_node

    def last(self, node):
        node.next = self.head
        self.head.pre = node

    def pop(self, cur_node):
        pre_node = cur_node.pre
        next_node = cur_node.next
        pre_node.next = next_node
        next_node.pre = pre_node
        return cur_node.num

N, K = map(int, input().split())
answer = []

linked_list = LinkedList()
node = linked_list.head

for n in range(1, N + 1):
    node = linked_list.append(node, n)

linked_list.last(node)
node = linked_list.head

while linked_list.head.next.next != linked_list.head:
    node = linked_list.turn_next(node, K)
    answer.append(linked_list.pop(node))
answer.append(linked_list.head.next.num)

print('<', end='')
print(', '.join(map(str, answer)), end='')
print('>')
