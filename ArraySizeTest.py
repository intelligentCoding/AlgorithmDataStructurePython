import sys

# set the value of N
n = 10

data = []

for i in range(50):
    # Here we are gonna find out the number of elements in the list
    a = len(data)
    #This ill tell us the size in bytes
    b = sys.getsizeof(data)

    print ('Length : ' + str(a) +  ' Size in bytes :' + str(b))

    #Now we will increase length by one
    data.append(n)



