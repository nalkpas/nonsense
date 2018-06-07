n = 12
    
def iterate(x):
    x = float(x)
    return 2 * x - n * x ** 2

result = 0.1
oldresult = -20
while (abs(result - oldresult) >= 10 ** (-10)):
    oldresult = result
    result = iterate(result)
    print oldresult, result
           
print(result)
print(1.0 / n) 