def convert(n):
    n = hex(n)
    print(n.replace('0x','').upper())

if __name__ == '__main__':
    convert(int(input()))
 
