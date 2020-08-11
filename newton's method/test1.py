n = 17

def f(x):
    x = float(x)
    return x ** 3 + 3*x + 1

def df(x): 
    x = float(x)
    return 3*x ** 2 + 3
    
def iterate(x):
    return x - f(x) / df(x)
    
def test(a):
    bottom = f(a - 10 ** (-n));
    top = f(a + 10 ** (-n));
    return (bottom * top <= 0)

result = -0.5
while not test(result):
    result = iterate(result)
    print f(result - 10 ** (-n)), f(result + 10 ** (-n)), f(result - 10 ** (-n)) * f(result + 10 ** (-n))
           
print(result)

n = 101

def f(x):
    return x ** 3 + 3*x + 1

def df(x): 
    return 3*x ** 2 + 3
    
def iterate(x):
    return x - f(x) / df(x)
    
def test(a):
    bottom = f(a - RealField(350)(10 ** (-n)));
    top = f(a + RealField(350)(10 ** (-n)));
    print bottom * top
    return (bottom * top <= 0)

result = RealField(350)(-0.5)
while not test(result):
    result = iterate(result)
           
result.n(digits = 100)