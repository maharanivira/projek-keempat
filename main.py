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

def statistik_mapel():
    """Fitur pengembangan: Menampilkan mapel favorit (paling banyak dipelajari)"""
    if len(catatan) == 0:
        print("Belum ada catatan belajar.\n")
        return
    
    # Hitung durasi per mapel
    durasi_per_mapel = {}
    for mapel_item in catatan:
        mapel_nama = mapel_item['mapel']
        if mapel_nama in durasi_per_mapel:
            durasi_per_mapel[mapel_nama] += mapel_item['durasi']
        else:
            durasi_per_mapel[mapel_nama] = mapel_item['durasi']
    
    # Urutkan mapel berdasarkan durasi terbanyak
    mapel_urutkan = sorted(durasi_per_mapel.items(), key=lambda x: x[1], reverse=True)
    
    print("\n⭐ === Statistik Mapel Favorit ===")
    for i, (mapel_nama, total_durasi) in enumerate(mapel_urutkan, 1):
        jam = total_durasi // 60
        menit = total_durasi % 60
        print(f"{i}. {mapel_nama}: {jam}j {menit}m ({total_durasi} menit)")
    
    print(f"\n🏆 Mapel Favorit: {mapel_urutkan[0][0]}\n")

def filter_mapel():
    """Fitur pengembangan: Filter dan tampilkan catatan berdasarkan mapel tertentu"""
    if len(catatan) == 0:
        print("Belum ada catatan belajar.\n")
        return
    
    # Minta input nama mapel dari user
    mapel_cari = input("Masukkan nama mapel yang ingin dicari: ")
    
    # Cari catatan dengan mapel yang diminta
    catatan_filter = [item for item in catatan if item['mapel'].lower() == mapel_cari.lower()]
    
    if len(catatan_filter) == 0:
        print(f"Tidak ada catatan untuk mapel '{mapel_cari}'.\n")
        return
    
    # Tampilkan catatan yang ditemukan
    print(f"\n🔍 === Catatan Untuk Mapel: {mapel_cari} ===")
    total_durasi = 0
    for i, item in enumerate(catatan_filter, 1):
        print(f"{i}. Topik: {item['topik']}")
        print(f"   Durasi: {item['durasi']} menit")
        total_durasi += item['durasi']
    
    # Tampilkan total waktu untuk mapel tersebut
    jam = total_durasi // 60
    menit = total_durasi % 60
    print(f"\n📊 Total waktu belajar {mapel_cari}: {jam}j {menit}m ({total_durasi} menit)\n")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("5. Statistik Mapel Favorit")
    print("6. Filter per Mapel")
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
    elif pilihan == "5":
        statistik_mapel()
    elif pilihan == "6":
        filter_mapel()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")
