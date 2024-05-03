class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return f"Angka {target} ditemukan"
            current = current.next
        return f"Angka {target} tidak ditemukan"
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

ll = LinkedList()
ll.add(9)
ll.add(4)
ll.add(3.5)
ll.add(8.2)
ll.add(2)
ll.display()
print(ll.search(4))
print(ll.search(8.3))

print("\nProgram Completed!\n\n--- By L200220277 ---")