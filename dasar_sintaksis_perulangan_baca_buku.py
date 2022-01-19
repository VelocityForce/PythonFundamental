"""
Program perulangan baca buku
"""
book_count = 7
read_count = 0
understood_count = 0
print('Ibu berkata, "baca semua buku"')
print(f"Jumlah buku yang sudah dibaca : {read_count}")

# Dengan For
# for read_count in range(1, book_count+1):
#     print(f"Buku ke {read_count} sudah dibaca")

# Dengan While
while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 6:
        print(f'"Buku ke {understood_count + 1} belum paham"')
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah dibaca dan dipahami")

if understood_count == book_count:
    print("Semua buku yang sudah dibaca dan dipahami")
else:
    print(f'"Tidak semua buku bisa dipahami, budi hanya bisa paham {understood_count} buku"')
