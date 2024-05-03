class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def cari(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def tambah_depan(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_akhir(self, data):
        if not self.head:
            self.tambah_depan(data)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(data)

    def tambah(self, data, posisi):
        if posisi == 0:
            self.tambah_depan(data)
            return
        new_node = Node(data)
        prev = None
        current = self.head
        for _ in range(posisi):
            if current is None:
                print("Posisi melebihi panjang linked list")
            prev = current
            current = current.next
        prev.next = new_node
        new_node.next = current

    def hapus(self, posisi):
        if posisi == 0:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        for _ in range(posisi):
            if current is None:
                print("Posisi melebihi panjang linked list")
            prev = current
            current = current.next
        prev.next = current.next

    # Method tambahan untuk mempermudah melihat hasil
    def cetak(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


ll = LinkedList()

ll.tambah_depan(9)
ll.tambah_depan(5.7)
ll.tambah_depan(2)
ll.cetak()

ll.tambah_akhir(4)
ll.cetak()

ll.tambah(3.5, 3)
ll.cetak()

print(ll.cari(9))
print(ll.cari(5))
ll.cetak()

ll.hapus(2)
ll.cetak()

print("\nProgram Completed!\n\n--- By L200220277 ---")
