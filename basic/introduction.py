import cmath




# Python Program to Find the Square Root
def Root(x):
    """Find the root of the given value"""
    root_vale = cmath.sqrt(x)
    if isinstance(root_vale, complex):
        print(f"the root value of {x} is a complex number")
    else:
        print(f"the root value is a real number")

    return root_vale





if __name__ == '__main__':
    num = complex(input("please enter a number to calculate the root value: "))
    root_num = Root(num)
    print(root_num)
