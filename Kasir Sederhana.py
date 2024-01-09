from datetime import datetime

# kode Rincian toko
toko_nama = "===== Warung Samsul ====="
toko_alamat = "Sawojajar"
toko_nomor_telepon = "08234989518"

# Daftar menu
daftar_menu = [
    {"nama": "Ayam Geprek", "harga": 12000},
    {"nama": "Ayam Bakar", "harga": 18000},
    {"nama": "Ayam Sambal Gurih", "harga": 15000},
    {"nama": "Ayam Kremes Kriuk", "harga": 20000},
    {"nama": "Air Mineral", "harga": 3000},
    {"nama": "Es Teh", "harga": 5000},
    {"nama": "Jeruk Nipis", "harga": 6000},
    {"nama": "Kopi Hitam", "harga": 7000},
]

# Tampilkan rincian toko
print(toko_nama)
print(toko_alamat)
print(toko_nomor_telepon)
print("=" * 29)

# Tampilkan daftar menu
print("Daftar Menu:")
for i, menu in enumerate(daftar_menu, start=1):
    print(f"{i}. {menu['nama']} ({menu['harga']} IDR)")

# Input pesanan
pesanan = {}
total_harga = 0

while True:
    pilihan = input("Pilih menu (1-8) atau ketik 'done' untuk mengakhiri pesanan: ")
    if pilihan.lower() == 'done':
        break
    elif not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(daftar_menu):
        print("Pilihan tidak valid.")
    else:
        indeks_menu = int(pilihan) - 1
        menu_terpilih = daftar_menu[indeks_menu]
        jumlah = input(f"Jumlah {menu_terpilih['nama']} yang dipesan: ")
        while not jumlah.isdigit() or int(jumlah) <= 0:
            print("Jumlah tidak valid. Harap masukkan angka positif.")
            jumlah = input(f"Jumlah {menu_terpilih['nama']} yang dipesan: ")
        jumlah = int(jumlah)
        total_harga += menu_terpilih['harga'] * jumlah
        pesanan[menu_terpilih['nama']] = jumlah

# Input uang dari pelanggan
uang_pelanggan = float(input("Input uang: "))

# Tampilkan struk
print("# Nama toko")
print(toko_nama)
print(toko_alamat)
print(toko_nomor_telepon)
print("=" * 29)
print("=" * 29)
print("Menu yang dipesan:")
for item, jumlah in pesanan.items():
    print(f"{item}: {jumlah}")
print("Total: ", total_harga)
print("Uang: ", uang_pelanggan)
print("Kembalian: ", uang_pelanggan - total_harga)
print("=" * 29)
print("Barang yang sudah dibeli tidak dapat dikembalikan")
print("=" * 29)
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))