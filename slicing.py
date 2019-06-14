my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,1

# list[start:end:step]
#x = int(2)

print (my_list[::-1])

sample_url = 'http://corey.com'
print (sample_url)

#reserve the url
print (sample_url[::-1])

#Get top level domain
print (sample_url[-4:])

#print url without http
print (sample_url[7:])

#print url without http or top level
print (sample_url[7:-4])