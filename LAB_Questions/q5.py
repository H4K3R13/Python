
list1 = [10, 21, 4, 45, 66, 93, 11]
 
even_nos = list(filter(lambda x: (x % 2 == 0), list1))
odd_nos = list(filter(lambda x: (x % 2 != 0), list1))
 
print("Even numbers in the list: ", even_nos)
print("\nOdd numbers in the list: ", odd_nos)