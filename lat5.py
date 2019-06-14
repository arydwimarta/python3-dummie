first = 'john'
last = 'smith'
message = first + ' [' + last.upper() + '] is a coder'
msg = f'{first.upper()} [{last}] is a coder' #f string
txt ='{} [{}] is a coder'.format(first,last.upper())
print (message)
print (msg)
print(txt)

print (dir(last)) # untuk menampilkan apa saja yang dapat digunakan oleh variabel tsb

print (help(int)) # menampilkan semua fungsi yang dapat dipakai

print (help(str.lower))