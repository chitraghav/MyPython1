#Approach 1
"""
limit = int(input())+1
for i in range(limit):
    print(' '*(limit-i),'#'*i)

'''
Average time taken = 7 minutes
'''
"""
#Approach 2
size = int(input())
for j in range(size):
        print(' '*(size-j-1),'#'*(j-1))
print('#'*(size-1))
print('#'*size)


'''
Average time taken = 17 minutes
'''
"""
#Approach 3
size = int(input())
for j in range(size):
    print('',' '*(size-j-1),'#'*(j-1)) if (size%2 ==0) else print(' '*(size-j-1),'#'*(j-1))   
print('#'*(size-1))
print('#'*size)
"""
'''
Average time taken = 12 minutes
'''
#Redo - Diamond
#Redo - without spaces
  
