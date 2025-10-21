import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def length(self):
        return self.size

    def addFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            new_node.next = current
            self.head = new_node
        self.size += 1

    def addLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        self.size += 1

    def addAfter(self, data, value):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.size += 1
            return
        else:
            current = self.head
            while current != None:
                if current.data == value:
                    new_node.next = current.next
                    current.next = new_node
                    self.size += 1
                    return
                else:
                    current = current.next
            print("Node dengan data", value, "tidak ditemukan")

    def display(self):
        if self.isEmpty():
            print("Linked list kosong")
        else:
            current = self.head
            while current != None:
                print(current.data, end=" ")
                current = current.next
            print()

    def searchNode(self, data):
        if self.isEmpty():
            print("Linked list kosong")
            return False
        current = self.head
        while current != None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False

    def deleteNode(self, data):
        if self.isEmpty():
            print("Linked list is empty, deletion failed")
            return
        if self.head.data == data:
            self.head = self.head.next
            print("Node with data", data, "is deleted")
            return
        current = self.head
        prev = None
        while current != None and current.data != data:
            prev = current
            current = current.next
        if current == None:
            print("Node with data", data, "not found")
            return
        prev.next = current.next
        print("Node with data", data, "is deleted")

    def deleteFirst(self):
        if self.isEmpty():
            print("Linked list is empty, deletion failed")
            return
        prev = self.head
        self.head = self.head.next
        return prev.data

    def deleteLast(self):
        if self.isEmpty():
            print("Linked list is empty, deletion failed")
            return
        elif self.head.next == None:
            data = self.head.data
            self.head = None
            return data
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            data = temp.next.data
            temp.next = None
            return data

    def deleteBack(self):
        if self.isEmpty():
            print("Linked list is empty, deletion failed")
            return
        temp = self.head
        if temp.next == None:
            data = temp.data
            self.head = None
            return data
        while temp.next.next != None:
            temp = temp.next
        data = temp.next.data
        temp.next = None
        return data


myList = LinkedList()
cek = True

while cek:
    print("\n-----------Masukan Pilihan Anda-----------")
    print("1. Tambah Elemen pada Linked List")
    print("2. Tampil Elemen dalam Linked List")
    print("3. Hapus Elemen dalam Linked List")
    print("4. Jumlah Elemen dalam Linked List")
    print("0. Keluar")
    print("------------------------------------------")

    pil = int(input('Masukan Pilihan anda: '))
    print()

    if pil == 1:
        temp = True
        while temp:
            print('-------Pilihan Tambah Data--------')
            print(' 1. Tambah Elemen di Awal Linked List')
            print(' 2. Tambah Elemen di Tengah Linked List')
            print(' 3. Tambah Elemen di Akhir Linked List')
            print('----------------------------------')
            print(' 0. Kembali ke Menu Utama')
            print()

            pilmenu = int(input('Masukan Pilihan anda: '))
            print()
            if pilmenu == 1:
                data = int(input('Masukan Data yang ingin ditambahkan: '))
                myList.addFirst(data)
                print(f'Data {data} berhasil ditambahkan di awal linked list')
            elif pilmenu == 2:
                data = int(input('Masukan Data yang ingin ditambahkan: '))
                value = int(input(f'Data {data} ingin ditambahkan setelah data apa?: '))
                myList.addAfter(data, value)
                print(f'Data {data} berhasil ditambahkan setelah {value}')
            elif pilmenu == 3:
                data = int(input('Masukan Data yang ingin ditambahkan: '))
                myList.addLast(data)
                print(f'Data {data} berhasil ditambahkan di akhir linked list')
            elif pilmenu == 0:
                temp = False
                break

    elif pil == 2:
        print("Isi Linked List:")
        myList.display()

    elif pil == 3:
        temp = True
        while temp:
            print('-------Pilihan Hapus Data--------')
            print(' 1. Hapus Elemen di Awal Linked List')
            print(' 2. Hapus Elemen di Tengah Linked List')
            print(' 3. Hapus Elemen di Akhir Linked List')
            print('----------------------------------')
            print(' 0. Kembali ke Menu Utama')
            print()

            pilmenu = int(input('Masukan Pilihan anda: '))
            if pilmenu == 1:
                hapus = myList.deleteFirst()
                print(f'Data {hapus} berhasil dihapus')
            elif pilmenu == 2:
                data = int(input('Masukan Data yang ingin dihapus: '))
                myList.deleteNode(data)
                print(f'Data {data} berhasil dihapus')
            elif pilmenu == 3:
                hapus = myList.deleteBack()
                print(f'Data {hapus} berhasil dihapus')
            elif pilmenu == 0:
                temp = False
                break

    elif pil == 4:
        print(f'Jumlah node dalam linked list: {myList.length()}')

    elif pil == 0:
        print('Bye.. Byee...!!')
        print()
        cek = False
        break

    else:
        print('Pilihan tidak ada')
