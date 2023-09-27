my_list = [10, 20, 30, 40, 50]
result = my_list[-3:]
print(result)

my_list = [1, 2, 3, 4, 5]
result = my_list[::2]
print(result)

# seclicig
my_list = ['apple', 'banana', 'cherry', 'date']
result = my_list[:-2]
print(result)

# exam
print(64/8)

fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
print(fruits)

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)

def greet(name):
    print("Hello, " + name + "!")


greet('abhi')


for i in range(1, 4):

    for j in range(i, i + 3):

        print(j, end=" ")

    print()

for i in range(1,6):
    print(i)


num = 10
if num % 2 == 0:
    result = "Even"
else:
    result = "Odd"
 
print(result)


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

string = "Hello, World!"

result = string.split(", ")

print(result[1])

x = 5
y = 10
if x > y:
     print("x is greater than y.")
elif x < y: print("x is less than y.")
else: print("x and y are equal.")

i = 1
while i <= 5:
    i += 1
    print(i)

age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
x = 5
y = 3
z = x + y
print(z)
