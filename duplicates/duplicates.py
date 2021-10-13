'''
Write a function to remove all the duplicates from the array and return a unique integer array.
'''
def remDupl(arr):
    # convert the array to set as it cant contain duplicates
    set1 = set(arr)
    # converting set to array(list) as you are required to output a array
    arr1 = list(set1)
    return arr1

# Driver code
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    print(remDupl(arr))