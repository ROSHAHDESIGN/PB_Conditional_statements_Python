# #print("it`s working ok")
# currency = input("What is the currency? ")
# quantity = float(input("What is the quantity? "))
#
# #control flow
# #if/elif/else
#
# if currency == "usd":
#     bgn = quantity * 1.85
#     print(f"In bgn = {bgn}")
# elif currency == "eur":
#     bgn = quantity * 1.95
#     print(f"In bgn = {bgn}")
#
# num = 12
# print(type(num)) #<class"int>
#
# num_as_string = str(num)
# print(num_as_string)
# print(type(num_as_string))

# 1. assignment
num = 12

# 2. cast
num2_as_string = "12"  # input()
num2 = int(num2_as_string)  # int(input())

print(num2)
print(type(num2))

# 3. run-time evauation -> math operators
num3 = 200 + 20.20
print(num3)
print(type(num3))

# 4.boolean()
name = "Rose"
is_not_empty = bool(name)
print(is_not_empty)  # True
print(type(is_not_empty))  # <class "bool">

# 5.boolean False is empty string " "

# 6. run-time evaluation -> using comparison operators
number = 1000

is_greater_then_100 = number > 100  # True
print(is_greater_then_100)
print(type(is_greater_then_100))

# 7. Boolean False is also bool(0) or bool(0.0) ;bool(' ') or bool(" ")


# if ; if-else ; if-elif-else ;
num5 = - 5

if num5 > 10:
    print("it is greater than 10")
    print("line 2 inside if")
elif num5 < 0:
    print("it is less than 0")
else:
    print("it is not greater")
