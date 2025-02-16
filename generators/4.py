def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2
a = int(input("Enter a number: "))
b = int(input("one more: "))
for num in squares(a, b):
    print(num)