teman = []

def tambah_nama():
    nama = input("Masukkan nama teman yang ingin ditambahkan: ")
    teman.append(nama)
    print(nama, "telah ditambahkan ke daftar teman.")

def hapus_nama():
    nama = input("Masukkan nama teman yang ingin dihapus: ")
    if nama in teman:
        teman.remove(nama)
        print(nama, "telah dihapus dari daftar teman.")
    else:
        print("Nama tidak ditemukan dalam daftar teman.")

def tampilkan_nama():
    print("Daftar Teman:")
    for nama in teman:
        print("-", nama)

while True:
    print("\nMenu:")
    print("1. Tambahkan nama")
    print("2. Hapus nama")
    print("3. Tampilkan nama")
    print("4. Exit")

    pilihan = input("Pilih opsi (1/2/3/4): ")

    if pilihan == '1':
        tambah_nama()
    elif pilihan == '2':
        hapus_nama()
    elif pilihan == '3':
        tampilkan_nama()
    elif pilihan == '4':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
