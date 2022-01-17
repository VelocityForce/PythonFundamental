# Percabangan
jumlah_botol_susu = 15
jumlah_telur = 10
uang_anak = 10000
harga_susu = 1000
harga_telur = 500

print(f"Jumlah botol susu : {jumlah_botol_susu} btl")
print(f"Jumlah telur : {jumlah_telur} btr")
print(f"Uang Budi : {uang_anak} rupiah")

print("\nBudi mengecek barang di toko")
if jumlah_botol_susu > 0:
    print("Susu terserdia")
    if 1 * harga_susu < uang_anak:
        print("Budi membeli 1 botol susu")
        uang_anak = uang_anak - (1 * harga_susu)
        jumlah_botol_susu = jumlah_botol_susu - 1
        if jumlah_telur > 0:
            if 6 * harga_telur <= uang_anak:
                print("Budi membeli 6 butir telur")
                uang_anak = uang_anak - (6 * harga_telur)
                jumlah_telur = jumlah_telur - 6
            else:
                print("Uang Budi kurang")
    else:
        print("Uang Budi kurang")
else:
    print("Budi langsung pulang tanpa membeli apa-apa")

print(f"\nJumlah botol susu : {jumlah_botol_susu} btl")
print(f"Jumlah telur : {jumlah_telur} btr")
print(f"Uang Budi : {uang_anak} rupiah")
