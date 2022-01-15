def kittufunc(size, arr):
    #size = int(input())
    #arr = []
    pos=0
    neg=0
    zero=0
    #arr = list(map(int, input().split(' ')[:size]))  # to input n elements
    print(arr)
    for i in range(size):
        if (int(arr[i])>0):
            pos +=1
        elif (int(arr[i])<0):
            neg +=1
        elif (int(arr[i]) == 0):
            zero +=1
    posRatio = pos/size
    negRatio = neg/size
    zeroRatio = zero/size
    print('Output ', '%.6f'%posRatio,'\n','{0:.6f}'.format(negRatio), '\n','{0:.6f}'.format(zeroRatio))

if __name__ == '__main__':
    size = int(input())
    arr = list(map(int, input().rstrip().split()))
    kittufunc(size, arr)

'''
Average time taken = 45 minutes
Points to ponder about (Findings):
Precising Handling in Python-> To print value till 2 decimal places
---print ('%.2f'%a)
---print ("{0:.2f}".format(a))
---print (round(a,2)) // This method deceits sometimes
---arr = list(map(int, input().rstrip().split())) /// to make it in a line
---if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
'''