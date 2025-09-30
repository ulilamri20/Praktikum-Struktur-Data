import os
from queue import LifoQueue
from collections import deque

print()
MaxSize = int(input("Masukan Jumlah data yang ingin ditambah: "))

DequeStack = deque()
LifoStack = LifoQueue(maxsize=MaxSize)

cek = True

while cek:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== MENU UTAMA ===")
    print("1. Stack dengan Deque")
    print("2. Stack dengan LifoQueue")
    print("0. Keluar")
    pil = int(input("Masukan Pilihan anda: "))

    if pil == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        temp = True
        while temp:
            print("\n=== STACK DEQUE ===")
            print("1. Tambah Data dengan Deque")
            print("2. Hapus Data Deque")
            print("3. Tampil Data Deque")
            print("4. Jumlah Data Deque")
            print("0. Kembali")
            pilMenu = int(input("Masukan pilihan anda: "))

            if pilMenu == 1:
                if len(DequeStack) < MaxSize:
                    i = len(DequeStack) + 1
                    while i <= MaxSize:
                        item = input(f"Masukan data ke-{i}: ")
                        DequeStack.append(item)
                        i += 1
                else:
                    print("Data tidak bisa ditambah. Stack sudah penuh!")
            
            elif pilMenu == 2:
                if len(DequeStack) != 0:
                    print(f"Elemen terakhir: {DequeStack.pop()} telah dihapus")
                else:
                    print("Stack kosong. Tidak ada elemen untuk dihapus!")
            
            elif pilMenu == 3:
                print("Data dalam Stack adalah:", list(DequeStack))
            
            elif pilMenu == 4:
                print(f"Jumlah Data dalam Stack = {len(DequeStack)}")
            
            elif pilMenu == 0:
                temp = False
                break
            
            else:
                print("Pilihan tidak ada!")

    elif pil == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        temp = True
        while temp:
            print("\n=== STACK LIFOQUEUE ===")
            print("1. Tambah Data dengan LifoQueue")
            print("2. Hapus Data LifoQueue")
            print("3. Tampil Data LifoQueue")
            print("4. Jumlah Data LifoQueue")
            print("0. Kembali")
            pilMenu = int(input("Masukan pilihan anda: "))

            if pilMenu == 1:
                if LifoStack.qsize() == 0:
                    i = 1
                else:
                    i = LifoStack.qsize() + 1

                if not LifoStack.full():
                    while i <= MaxSize:
                        item = input(f"Masukan data ke-{i}: ")
                        LifoStack.put(item)
                        i += 1
                else:
                    print("Data tidak bisa ditambah. Stack sudah penuh!")

            elif pilMenu == 2:
                if not LifoStack.empty():
                    print(f"Elemen terakhir: {LifoStack.get()} telah dihapus")
                else:
                    print("Stack kosong. Tidak ada elemen untuk dihapus!")
            
            elif pilMenu == 3:
                isi = list(LifoStack.queue)
                print("Data dalam Stack adalah:", isi)
            
            elif pilMenu == 4:
                print(f"Jumlah Data dalam Stack = {LifoStack.qsize()}")
            
            elif pilMenu == 0:
                temp = False
                break
            
            else:
                print("Pilihan tidak ada!")

    elif pil == 0:
        cek = False
        break

    else:
        print("Pilihan tidak ada!")