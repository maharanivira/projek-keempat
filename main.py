catatan = []

def tambah_catatan():
    # Meminta input dari pengguna
    mapel = input("Masukkan nama mapel: ")
    topik = input("Masukkan topik yang dipelajari: ")
    durasi = int(input("Masukkan durasi belajar (menit): "))
    
    # Membuat catatan dalam bentuk dictionary
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    
    # Menambahkan catatan ke list
    catatan.append(catatan_baru)
    
    print(f"✓ Catatan belajar {mapel} berhasil ditambahkan!\n")

def lihat_catatan():
    if len(catatan) == 0:
        print("Belum ada catatan belajar.\n")
        return
    
    print("\n=== Daftar Catatan Belajar ===")
    for i, item in enumerate(catatan, 1):
        print(f"{i}. Mapel: {item['mapel']}")
        print(f"   Topik: {item['topik']}")
        print(f"   Durasi: {item['durasi']} menit\n")

def total_waktu():
    if len(catatan) == 0:
        print("Belum ada catatan belajar.\n")
        return
    
    total = sum(item['durasi'] for item in catatan)
    jam = total // 60
    menit = total % 60
    
    print(f"\n📊 Total waktu belajar: {jam} jam {menit} menit ({total} menit)\n")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")
