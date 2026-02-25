# TASK1
number = int(input('Enter a number:'))
if number % 2 == 0:
     print(f'The number {number} is even.')
else:
     print(f'The number {number} is odd.')

# TASK2
n=0
for i in range(51):
    n+=i
    print(n)

print(f'The sum of numbers from 1 to 50 is : {n}.')