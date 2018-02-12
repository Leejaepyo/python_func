def scope_test():
    global a  #전역변수
    a=1
    print('a:{0}'.format(a))
scope_test()
print('a:{0}'.format(a))

print()

#재귀함수
def factorial(n):
    if n==0:
        return 1
    elif n>0:
        return factorial(n-1)*n

print(factorial(3))
print(factorial(5))
print(factorial(10))
print(factorial(100))



babo=factorial

print(babo(3))

print()

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

flist=[plus,minus]
print(flist[0](1,2))


print()

import math
def stddev(*args):
    def mean():
        return sum(args)/len(args)

    def variance(m):
        total=0
        for arg in args:
            total +=(arg-m)**2
        return total/(len(args)-1)
    v=variance(mean())
    return math.sqrt(v)

print(stddev(2.3, 1.7, 1.4, 0.7, 1.9))




