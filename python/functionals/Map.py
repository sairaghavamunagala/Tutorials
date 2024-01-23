def addition(n)->int:
    return n + n
 

numbers = (1, 2, 3, 4,5)
result = map(addition, numbers)
print(type(result))
print(result)
print(list(result))
print("Implementation using lambda")
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))