daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika']
print("Tampilkan variable daftar_buku")
print(daftar_buku)

print('\nTampilkan dengan For')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan berdasarkan index')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTampilkan dengan for in range, dan tipe data tiap element berbeda')
daftar_buku = [7, 'Bahasa Indonesia', -3.14, 'Budi']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan value semula')
daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika']
print('\nTambahkan 1 buku lagi')
daftar_buku.append('English')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list')
daftar_buku.clear()
print(f'Jumlah buku = {daftar_buku.count(int)} buku')

print('\nGanti data pada element ke 2')
daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika', 'English']
daftar_buku[1] = 'Biologi'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil buku dari element ke 1 dan masukan ke variable')
# Ambil dan masukan ke variable
buku_ambil = daftar_buku.pop(0)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTampilkan buku yang di ambil')
print(buku_ambil)

print('\nAmbil buku dengan Pop tanpa parameter, data akan diambil dari paling akhir')
daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika', 'English']
# Ambil tanpa parameter
buku_ambil = daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print(f'\nBuku terakhir = {buku_ambil}')

print('\nAmbil buku dengan Pop menggunakan parameter minus (-),'
      ' data akan diambil dengan hitung element dari paling akhir, -1 adalah untuk data pertama dari belakang')
daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika', 'English']
# Ambil denga parameter minus
buku_ambil = daftar_buku.pop(-3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print(f'\nBuku diambil = {buku_ambil}')
