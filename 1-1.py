'''
Palindrome
==========
To help Beta Rabbit crack the lock, write a function answer(n) which returns the
smallest positive integer base b, at least 2, in which the integer n is a
palindrome. The input n will satisfy "0 <= n <= 1000".

'''
#Function creates list with figures in base b for integer n
def convbasefunc(n,b):
    l=[]
    L=[]
    m=n
    if m>0:
        while m>0:
            l.append((m%b))
            m=m//b
        L=l[::-1]
    else:
        L.append(0)
    return L

#Function finds the smallest base for integer n where n is a palindrome
def answer(n):
    b=2
    while True:
        x=convbasefunc(n, b)
        if x==x[::-1]:
            break
        else:
            b=b+1
    return b

while True:
    line = input('Enter a number:')
    if line=='done':
        break
    try:
        n=int(line)
        b=answer(n)
        print(b)
    except:
        print ("Invalid input")


'''
n=0
while n<1001:
    b=answer(n)
    print(n, b)
    n=n+1
'''