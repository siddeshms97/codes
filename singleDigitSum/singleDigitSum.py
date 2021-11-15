# write a program to display single digit sum of entered numbers, 89 = 8 + 9 = 1 + 7 = 8
def summ(n):
    num = str(n)
    if len(num) > 1:
        sumOfDigits(num)
    else:
        print(n)

def sumOfDigits(num):
    s = 0
    for digit in num:
        s += int(digit)
    summ(s)

if __name__ == '__main__':
    num = int(input())
    summ(num)
