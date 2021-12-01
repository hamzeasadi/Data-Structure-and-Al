import cmath
import math




# Python Program to Find the Square Root
def Root(x):
    """Find the root of the given value"""
    try:
        x = float(x)
        if isinstance(x, complex) or x<0:
            root_val = cmath.sqrt(x)
            print(f"the root value of given number, {x} is a complex number: {root_val}")
        else:
            root_val = math.sqrt(x)
            print(f"the root value of given number, {x} is a real number: {root_val:.4f}")
    except Exception as e:
        x = complex(x)
        print(f"the input value was an complex number: {x}")
        root_val = cmath.sqrt(x)
        print(f"the root value of given number, {x} is a complex number: {root_val}")

# Python Program to Find the Square Root based on eval function

def RootEval(x):
    x = eval(x)
    if isinstance(x, complex) or x<0:
        print(f"the square root of {x} is {cmath.sqrt(x)}")
    else:
        print(f"the square root of {x} is {math.sqrt(x)}")

# Python Program to Calculate the Area of a Triangle
def AreaTriangle(*x):

    if len(x) != 3:
        raise ValueError
    else:
        x = sorted(x)
        if x[-1] < (x[0] + x[1]):
            perimeter = sum(x)/2
            area = perimeter
            for val in x:
                area *=(perimeter - val)
            return math.sqrt(area)
        else:
            print("with given values is impossible to build a triangle")


# Python Program to Solve Quadratic Equation
def QuadraticSolution(**coefficients):
    """
    Please input coefficients of the equation by following conventions
    a=coefficient vale of x2
    b=coefficient value of x
    c=constant coefficient
    """
    a, b, c = coefficients['a'], coefficients['b'], coefficients['c']
    delta = cmath.sqrt(b**2 - 4*(a*c))
    ans1 = (-b - delta)/(2*a)
    ans2 = (-b + delta)/(2*a)
    print(f"answers for {a}x2 - {b}x + {c} = 0 : {ans1:.3f} and {ans2:.3f}")







if __name__ == '__main__':
    a, b, c = input("enter quadratic equation coefficients (seperate values with ','): ").split(sep=',')
    coef = dict(a=eval(a), b=eval(b), c=eval(c))
    QuadraticSolution(**coef)
