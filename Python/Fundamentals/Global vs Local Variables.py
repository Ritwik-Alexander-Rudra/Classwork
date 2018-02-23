#Local can only be accessed within its environment
#You can turn local variables into a local variable

x = 6
def example():
    #globe x
    print(x)
    print(x + 5)
    #x += 2 would cause an error if you didn't have 'global x' in the beginning


def example2():
    globx = x
    print(globx)
    globx += 5
    print (globx)
    return globx


x = example2()
print(x)
