'''
*****
****
***
**
*
'''

def factorial(n):

    if n==0:
        return 1
    elif n>0:
        for i in range(n):
            print("*",end=" ", )
        print()
        return factorial(n-1)


factorial(5)