#1. Write a function to add two numbers.

def add(a,b):
    return a+b
print(add(2,3))

#2. Function to check prime number.

def is_prime():
    a=int(input("enter number: "))
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print(a,"is not a prime number")
                break
        else:
            print(a,'is a prime number')
    else:
        print(a,'is not a prime number')
is_prime()

#-------LOGIC-------
'''
🔸 Step 1:First, take a number (let's say num) from the user.

🔸 Step 2:Check if the number is greater than 1.
        Because:Numbers less than or equal to 1 (like 0, 1, or negative numbers)are not prime.

🔸 Step 3:Now, try dividing the number by all numbers from 2 to (a - 1).
        If any of these numbers divide it completely (i.e., remainder is 0),
            ➤ Then it is NOT a prime number.
        If none of these numbers divide it,
            ➤ Then it IS a prime number.
'''

#3. Function to find factorial (loop).

def fact(result=1):
    n=int(input('enter number:'))
    for i in range(1,n+1):
        result*=i
    return result  
print(fact())
        
        
        
#4. Function to find factorial (recursion).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))


#5. Function to generate Fibonacci series.

def fab(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number: "))
fab(n)

#6. Function to check palindrome number.

def palindrome(n):
    if n==n[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
n=input('enter number:')
palindrome(n)

#7. Function to check Armstrong number.

def is_armstrong(num):
    power = len(str(num))  
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10          
        total += digit ** power     
        temp //= 10                 
    if total == num:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

n = int(input("Enter a number: "))
is_armstrong(n)


#8. Function to find GCD of two numbers.
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD is:", find_gcd(x, y))

#9. Function to calculate sum of digits.

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10   
        n //= 10
        return total

num = int(input("Enter a number: "))
print("Sum of digits is:", sum_of_digits(num))

#10. Function to calculate power of number.

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

print(f"{b}^{e} =", power(b, e))
