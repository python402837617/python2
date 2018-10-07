def total(a=5,*numbers,**phonebook):
    print('a',a)
    for b in numbers:
        print('b',b)
    for c,d in phonebook.items():
        print(c,d)
total(10,1,2,3,jack=1123,jonh=1254,inge=5412)

def f1(x):
    return x
print(f1(2))
def print_1(x):
    '''Aisme.

    lalalalaal'''
    return x
print(print_1(5))
help(print_1)
print(__name__)