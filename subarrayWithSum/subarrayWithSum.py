'''
Given an unsorted array A and size N that contains only non-negative integers, find continuous 
sub-array which adds to a given sum S.

Input:
1. N (integer)
2. S (integer)
3. A[] (integer array)

Output:
1. starting and ending index of sub array
'''
def subarraySum(A,N,S):
    for i in range(N):
        summ = A[i]
        j = i+1
        while j <= N:
            if summ == S:
                print(f'{i} {j-1}')
                return 1
            if summ > S and j == N:
                break
            summ = summ + A[j]
            j += 1
    print(-1)
    return 0

if __name__ == '__main__':
    N = int(input())
    S = int(input())
    A = list(map(int,input().split()))
    subarraySum(A,N,S)
    