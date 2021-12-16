#Python program to find a pair with highest product from a given array of integers.
def max_product(arr):
    length = len(arr)
    if(length<2):
        print("No pair Exists")
        return
    x=arr[0];y=arr[1]
    #traversing the array with every possible pair
    for i in range(0,length):
        for j in range (i+1,length):
            if(arr[i] *arr[j] > x*y):
                x= arr[i];y=arr[j]
    return x,y
num = [1,2,3,4,7,0,8,4]
print("Array values: ",num)
print("Maximum Product pair: ",max_product(num))
