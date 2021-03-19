#Soal 2
#Titus Kurniawan Sandy Purwanto
#I0320102
#Kelas C

dict = {'Nama' : ['Titus'],
        'Hobi' : ['Bermain basket', 'tidur', 'makan'],
        'Sosial media' : ['Instagram', 'line', 'Twitter'],
        'Lagu kesukaan' : ['Save Your Tears', 'Loving is easy'],
        'Makanan favorit' : ['Nasi goreng', 'soto', 'magelangan']}
print(dict)

#Ubah salah satu hobi & media sosial
dict['Hobi'][0] = 'Menonton film'
dict['Sosial media'][0] = ('Facebook')

#Hapus dua makanan favorit
del dict['Makanan favorit'][1:3]

#Menambahkan satu hobi
dict['Hobi'].append('Mendengarkan musik')



print(dict)