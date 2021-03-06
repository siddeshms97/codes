'''
Sum of Letters

During a class assessment, a teacher asks students to solve the following
problem IfA=0,B=1.C=B+A, D=C+B, and so on, find the sum of the alphabets of a given word

Input Specification:
input1: String representing any word

Output Specification:
Return an integer value which represents the sum of all the alphabets in input1, as per the 
above-given scenario
'''
def SOL(str):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    values = [0,1]
    x,y = values[0], values[1]
    sum = 0
    for i in range(2,26):
        values.append(x + y)
        y = values[i]
        x = values[i - 1]
    for i in str:
        indexx = letters.index(i)
        sum += values[indexx]
    return sum

if __name__ == '__main__':
    str = input().upper()
    print(SOL(str))