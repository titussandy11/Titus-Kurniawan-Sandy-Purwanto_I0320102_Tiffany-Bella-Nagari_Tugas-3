#Soal 1
#Titus Kurniawan Sandy Purwanto
#I0320102
#Kelas C

list = ['Issa', 'Nauval', 'Sekar', 'Harry', 'Tito', 'Soni', 'Ivan', 'Togar', 'Angga', 'Muhammad']
print("Isi list pada index nomor [4, 6, 7] :", list[4], list[6], list[7])

list[3] = 'Dias'
list[5] = 'Albert'
list[9] = 'Alex'

list.append('David')
list.append('Gagarin')

print("Teman-temanku adalah : ")
for temanku in list :
    print(temanku)
print("Jumlah dari temanku ada", len(list), "orang")