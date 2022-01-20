print('\nPerintah del')
daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika', 'English']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nPerintah del dengan list comprehension')
daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika', 'English']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nPerintah del dengan list comprehension Start')
daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika', 'English']
del daftar_buku[0:-2] # Start:End
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nPerintah del dengan list comprehension Start:End:Step')
daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika', 'English', 'Kimia', 'Biologi', 'Sosiologi']
del daftar_buku[0::2] # Start:End:Step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan comprehension')
daftar_buku = ['Matematika', 'Bahasa Indonesia', 'Fisika', 'English', 'Kimia', 'Biologi', 'Sosiologi']
daftar_buku_baru = daftar_buku[2:] # Start:End:Step
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])


print('\nMembuat list baru dengan comprehension : Ganjil')
daftar_buku = ['1 Matematika', '2 Bahasa Indonesia', '3 Fisika', '4 English', '5 Kimia', '6 Biologi', '7 Sosiologi']
daftar_buku_baru = daftar_buku[0::2] # Start:End:Step
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])


print('\nMembuat list baru dengan comprehension : Genap')
daftar_buku = ['1 Matematika', '2 Bahasa Indonesia', '3 Fisika', '4 English', '5 Kimia', '6 Biologi', '7 Sosiologi']
daftar_buku_baru = daftar_buku[1::2] # Start:End:Step
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : Buang diujung')
daftar_buku = ['1 Matematika', '2 Bahasa Indonesia', '3 Fisika', '4 English', '5 Kimia', '6 Biologi', '7 Sosiologi']
daftar_buku_baru = daftar_buku[0:-1:2]  # Start:End:Step
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])



