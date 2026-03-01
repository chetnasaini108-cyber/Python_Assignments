#Task1 :Calculate Factorial using a function
def fact_rec(num):
    if num==1:
        return 1
    else:
        factorial = num*fact_rec(num-1)
        return factorial
num =int(input('Enter a number: '))
print(f'Factorial of number {num} is {fact_rec(num)}')



