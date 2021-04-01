#  Program harus dapat menerima input nama dan jenis kelamin pengguna program
nama = input('Masukkan nama anda :')
jenis_kelamin = input('Masukkan jenis kelamin(P/L) :').upper()

# Program menggunakan percabangan
# Program wajib memberikan output kepada pengguna berupa kalimat :
if jenis_kelamin == 'P':
	print('Selamat datang, Nyonya', nama)
elif jenis_kelamin == 'L':
	print('Selamat datang, Tuan', nama)
else:
	pass
print()