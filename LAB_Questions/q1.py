def squareRoot(n, l) :
    x = n
    count = 0
 
    while (1) :
        count += 1
        root = 0.5 * (x + (n / x))
 
        # Check for closeness
        if (abs(root - x) < l) :
            break
 
        # Update root
        x = root
 
    return root
# Bisection Method
 
def f(x, p, num):
 
    return pow(x, p) - num
 
def f_prime(x, p):
 
    return p * pow(x, p - 1)
 

def root(num, p):
 
   
    left = -num
    right = num
 
    x = 0
    while (True):
 
       
        x = (left + right) / 2.0
        value = f(x, p, num)
        prime = f_prime(x, p)
        if (value * prime <= 0):
            left = x
        else:
            right = x
        if (value < 0.000001 and value >= 0):
            return x

#n = 327
print("Find The Root Using Newton Raphson Method")
n=int(input("\nEnter The Number:"))
l = 0.00001
print(squareRoot(n, l))

print("\nFinding The Nth Root Using Bisection Method")
P = int(input("\nEnter The Number:"))
N = int(input("\nEnter N for the Nth Root:"))
ans = root(P, N)
print(ans)
