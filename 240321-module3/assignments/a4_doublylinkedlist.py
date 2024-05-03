class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def kunjungi_maju(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def kunjungi_mundur(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev

    def tambah_depan(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def tambah_akhir(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

dll = DoublyLinkedList()

dll.tambah_depan(8)
dll.tambah_depan(3)
dll.tambah_akhir(10)
dll.kunjungi_maju()
print("")
dll.tambah_depan(7.5)
dll.kunjungi_mundur()

print("\nProgram Completed!\n\n--- By L200220277 ---")
