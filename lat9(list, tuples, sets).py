courses = ['History', 'Math', 'Physics','CompSci']
courses_2 = ['Art','Education']
nums = [4,2,5,3,1]
#courses.append('test') #memasukkan value pada akhir list
#courses.insert(1,'dua') #memasukkan value sesuai dengan lokasi request
#courses.extend(courses_2) #memasukkan list kedalam list
#print (courses)
#courses.remove('Math') #menghapus salah satu value dari list
print(courses)
print(nums)
#print(courses)
#courses.pop() #menghilangkan last value pada list
#popped = courses.pop() #mengambil list terakhir
#print(popped)
#courses.reverse() #mengubah urutan list
#courses.sort() #mengurutkan berdasarkan alfabet
#nums.sort() #mengurutkan angka kecil - besar
#print(nums)
#nums.sort(reverse=True) #mengurutkan angka besar-kecil
#print(nums)
#new_sorted = sorted(courses) #teknik sortasi lain dengan menjaga original variabel
#print(new_sorted)
#print(min(nums)) #menampilkan angka terkecil = print(max(nums)) terbesar
#print(sum(nums)) #menjumlahkan keseluruhan list
#print(courses.index('Math')) #menunjukkan lokasi index
#print ('Art' in courses) #mengecek apakah terdapat didalam list atau tidak (False / True)
"""/* if ('ngek' in courses) :
    print ('True')
else:
    print ('False')"""

"""for baris in courses:
    print(baris) # print list in line per line

for index, baris in enumerate(courses, start=1): # print list in line disertai dengan nomor index
    print(index, baris)"""
courses_str = ' - '.join(courses) #menggabung list menjadi string yang terpisah dengan koma
print(courses_str)
new_list = courses_str.split(' - ') #mengembalikan sting menjadi list
print(new_list)
#print(help(str.split))
