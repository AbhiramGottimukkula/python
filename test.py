a = [1,2,-1,-2,-5,6,-9,7,-8]

def printArr(arr, n):
    for i in range(n):
        print arr[i]

def rearrange(arr, n):
    i = -1
    for j in range(n):
        if (arr[j] < 0):
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    printArr(arr, n)        



n = len(a)
rearrange(a, n)

