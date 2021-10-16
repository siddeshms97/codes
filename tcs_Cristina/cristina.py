def test(n):
    for i in range(2,n):
        x = digits(i)
        if i == x:
            print(i)
    return 0
        
def digits(x):
    sum = 0
    for digit in str(x):
        sum += (int(digit)*int(digit)*int(digit))
    return sum

if __name__ == '__main__':
    test(int(input()))