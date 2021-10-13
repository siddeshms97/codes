'''
String Permutation:

You are given two strings 'x' and 'y' each containing atmost 1000 characters.
write a program that can determine whether the charecter in the first string 'x' can be re-arranged
to form the second string 'y'. The output should be 'yes' if possible else 'no'.

'''
def perm(x,y):
    l1 = len(x)
    l2 = len(y)
    # if lengths are different then the string 'x' cant be re arranged to form 'y'
    if l1 != l2:
        print('no')
        return 0
    else:
        # sorting strings will ease the task of comparing the strings.
        str1 = sorted(x)
        str2 = sorted(y)
        if str1 == str2:
            print('yes')
            return 1

# Driver code
if __name__ == '__main__':
    x = input()
    y = input()
    perm(x,y)
            