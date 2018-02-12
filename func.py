def my_abs(arg):
    if(arg<0):
        result=arg*-1
    else:
        result=arg
    return result

print(my_abs(-5))
print(my_abs(10))

def print_string(text,count=1):
    for i in range(count):
        print(text)

print_string('안녕하세요',3)

#가변 매개변수
def merge_string(*text_list):
    result=''
    for s in text_list:
        result=result+s
    return result

print(merge_string('아버지가', '방에', '들어가신다.'))

#return
def my_abs(arg):
    if arg<0:
        return arg*-1
    else:
        return arg
result=my_abs(-1)
print(result)

def print_something(*args):
    for s in args:
        print(s)

print_something(1,2,3,4,5)
