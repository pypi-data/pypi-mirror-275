def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def factorial(n):
    if n < 0:
        return "Input should be a non-negative integer."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def palindrome(s):
    s = s.lower()
    s = ''.join([i for i in s if i.isalnum()])
    return s == s[::-1]

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def isArmstrong(n):
    s = str(n)
    return n == sum([int(i)**len(s) for i in s])

def isPerfect(n):
    return n == sum([i for i in range(1, n) if n % i == 0])

def isStrong(n):
    s = str(n)
    return n == sum([factorial(int(i)) for i in s])

def isHappy(n):
    def sumOfSquares(n):
        return sum([int(i)**2 for i in str(n)])
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sumOfSquares(n)
    return n == 1

def isHarshad(n):
    return n % sum([int(i) for i in str(n)]) == 0

def isPronic(n):
    for i in range(int(n**0.5)+1):
        if i*(i+1) == n:
            return True
    return False

def isAbundant(n):
    return sum([i for i in range(1, n) if n % i == 0]) > n

def isDeficient(n):
    return sum([i for i in range(1, n) if n % i == 0]) < n

def legrangeInterpolation(x, y, x0):
    n = len(x)
    if len(y) != n:
        return "The lengths of x and y should be the same."
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x0 - x[j]) / (x[i] - x[j])
        result += term
    return result

def newtonInterpolation(x, y, x0):
    n = len(x)
    if len(y) != n:
        return "The lengths of x and y should be the same."
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(i):
            term *= (x0 - x[j])
        result += term
    return result

def bisection(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        return "The function values at a and b should have opposite signs."
    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return "The method did not converge."

def newtonRaphson(f, df, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return "The method did not converge."

def secant(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return "The method did not converge."

def lagrangePolynomial(x, y):
    n = len(x)
    if len(y) != n:
        return "The lengths of x and y should be the same."
    def L(i, x0):
        result = 1
        for j in range(n):
            if j != i:
                result *= (x0 - x[j]) / (x[i] - x[j])
        return result
    def P(x0):
        return sum([y[i] * L(i, x0) for i in range(n)])
    return P

def newtonPolynomial(x, y):
    n = len(x)
    if len(y) != n:
        return "The lengths of x and y should be the same."
    def dividedDifference(i, j):
        if i == j:
            return y[i]
        return (dividedDifference(i+1, j) - dividedDifference(i, j-1)) / (x[j] - x[i])
    def P(x0):
        result = 0
        for i in range(n):
            term = dividedDifference(0, i)
            for j in range(i):
                term *= (x0 - x[j])
            result += term
        return result
    return P

def trapezoidalRule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i*h)
    return h * result

def simpsonsRule(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + i*h) if i % 2 == 0 else 4 * f(a + i*h)
    return h / 3 * result   

def eulerMethod(f, a, b, y0, n):
    h = (b - a) / n
    x, y = a, y0
    for i in range(n):
        y += h * f(x, y)
        x += h
    return y

def rungeKuttaMethod(f, a, b, y0, n):
    h = (b - a) / n
    x, y = a, y0
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
    return y

def trapezoidalRule2D(f, a, b, c, d, nx, ny):
    hx = (b - a) / nx
    hy = (d - c) / ny
    result = 0.25 * (f(a, c) + f(a, d) + f(b, c) + f(b, d))
    for i in range(1, nx):
        result += 0.5 * (f(a + i*hx, c) + f(a + i*hx, d))
    for j in range(1, ny):
        result += 0.5 * (f(a, c + j*hy) + f(b, c + j*hy))
    for i in range(1, nx):
        for j in range(1, ny):
            result += f(a + i*hx, c + j*hy)
    return hx * hy * result

def simpsonsRule2D(f, a, b, c, d, nx, ny):
    hx = (b - a) / nx
    hy = (d - c) / ny
    result = f(a, c) + f(a, d) + f(b, c) + f(b, d)
    for i in range(1, nx):
        result += 2 * (f(a + i*hx, c) + f(a + i*hx, d))
    for j in range(1, ny):
        result += 2 * (f(a, c + j*hy) + f(b, c + j*hy))
    for i in range(1, nx):
        for j in range(1, ny):
            result += 4 * f(a + i*hx, c + j*hy)
    return hx * hy / 9 * result

def eulerMethod2D(f, a, b, c, d, x0, y0, nx, ny):
    hx = (b - a) / nx
    hy = (d - c) / ny
    x, y = a, b
    for i in range(nx):
        for j in range(ny):
            x0 += hx * f(x, y, x0, y0)
            y0 += hy * f(x, y, x0, y0)
            x += hx
        x = a
        y += hy
    return x0, y0

def developer():
    print("This module is developed by Gautham Nair.")
    print("Email: gautham.nair.2005@gmail.com")