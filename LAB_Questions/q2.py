def isPalRec(st, s, e) :
     
    if (s == e):
        return True
 
    if (st[s] != st[e]) :
        return False
 
    if (s < e + 1) :
        return isPalRec(st, s + 1, e - 1)
 
    return True
 
def isPalindrome(st) :
    n = len(st)
    if (n == 0) :
        return True
     
    return isPalRec(st, 0, n - 1)
 
print("Program to check given string is palindrome or not:")
st = input("\nEnter The String:\n").lower()

if (isPalindrome(st)) :
    print("Yes")
else :
    print("No")