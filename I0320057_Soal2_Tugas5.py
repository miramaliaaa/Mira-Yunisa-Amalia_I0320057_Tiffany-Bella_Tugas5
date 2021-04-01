# Program harus dapat menerima input nama pengguna dan nilai yang berupa angka
nama = input('Masukkan nama anda :')
n = int(input('Masukkan nilai anda :'))

# Program wajib memberikan output kepada pengguna berupa kalimat :
info = 'Halo, ' + nama + '! Nilai anda setelah dikonversikan adalah '

# Program mengunakan percabangan
if n < 60:
    print(info + 'E')
elif n < 65:
    print(info + 'C')
elif n < 70:
    print(info + 'C+')
elif n < 75:
    print(info + 'B')
elif n < 80:
    print(info + 'B+')
elif n < 85:
    print(info + 'A-')
elif n <= 100:
    print(info + 'A')
else:
    pass
print()