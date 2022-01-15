size = int(input('Enter the size of the matrix: ')) 
print('Now, Enter the array elements: ')
matrix = {}
leftToRight = 0
rightToLeft = 0
for i in range(0,size): 
    for j in range(0,size): 
        value= input() 
        matrix.update({(i,j): value}) 
        if (i == j):
            leftToRight += int(matrix.get((i,j)))
            #print(leftToRight)
print(matrix)
for k in range(0,size):
    rightToLeft += int(matrix.get((size-k-1,k)))
    #print(rightToLeft)

absDifference = abs(leftToRight-rightToLeft)
print('**********')
print('The absolute diagonal difference of your matrix is: ', absDifference)
print('**********')




    
            





'''
Rough draft
#leftToRight
#def diagonalDifference(arr):
order= str(size-i)
            rightToLeft += matrix.get((order,i))
            print(rightToLeft)

            order = size-k-1
    print('Order ', order)
'''

