import os
import time
import math

# array rudi
rudi = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]


def jump():
    def jump(arr, x):
        panjang = len(arr)
        jump = int(math.sqrt(panjang))
        kiri, kanan = 0, 0
        while kiri < panjang and arr[kiri] <= x:
            kanan = min(panjang - 1, kiri + jump)
            if arr[kiri] <= x and arr[kanan] >= x:
                break
            kiri += jump
        if kiri >= panjang or arr[kiri] > x:
            return -1
        kanan = min(panjang - 1, kanan)
        i = kiri
        while i <= kanan and arr[i] <= x:
            if arr[i] == x:
                return i
            i += 1
        return -1

    print("\nDaftar Data: ", rudi)
    time.sleep(1)

# Cari Arsel
    Arsel = jump(rudi, "Arsel")
    if Arsel != -1:
        print("Arsel di Index", Arsel)
# Cari Avivah
    Avivah = jump(rudi, "Avivah")
    if Avivah != -1:
        print("Avivah di Index", Avivah)
# Cari Daiva
    Daiva = jump(rudi, "Daiva")
    if Daiva != -1:
        print("Daiva di Index", Daiva)
# Cari Wahyu
    Wahyu = jump(rudi[3], "Wahyu")
    if Wahyu != -1:
        print("Wahyu di Index 3 pada kolom 0")
# Cari Wibi
    Wibi = jump(rudi[3], "Wibi")
    if Wibi != -1:
        print("Wibi di Index 3 pada kolom 1")


def Gass():
    while True:
        os.system("cls")
        print('''
              \tProgram serching
              \tData-data yang akan dicari indeksnya:
              \tArsel, Avivah, Daiva, Wahyu, Wibi
              \tSilahkan pilih metode searchingnya
              ''')
        menu = input("\tPilih:\t1.JumpSearch\t2.Exit2\n\t:")
        if menu == "1":
            jump()
            input("Tekan Enter untuk kembali")
            os.system("cls")
            Gass()
            break
        elif menu == "2":
            print("Anda telah keluar")
            break


Gass()
