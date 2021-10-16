'''
To reduce the impact of waste on Earth, a Red Day Sale is open to the public in one of the leading 
clothing outlets. People wait for this day to buy apparels of their favorite
brands at the lowest cost. The only condition to buy any1160 clothing on Red Day Sale is through
coupons from the store. A coupon can be obtained by exchanging any old/used clothes for a coupon.
The task here is to find the maximum number of coupons you can use such that: O number of old clothes
should be exchanged to receive one coupon. One coupon can be used to buy one piece of clothing only.

Example 1:

Input:
4 → number of coupons
2 → old clothes

Output:
7 → Maximum coupons that can be obtained
'''

def maxCoupons(c,o):
    newclothes = count = c # 1 coupon = 1 new cloth, number of coupons = count 
    o = o + newclothes     # new clothes(conciderd as old) can also be exchanged to get coupons
    count = count + (o//2) # for two old clothes 1 coupon
    return count

if __name__ == '__main__':
    c = int(input())       # coupons
    o = int(input())       # old clothes
    print(maxCoupons(c,o))