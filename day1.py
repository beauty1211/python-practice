#Q1. Print hello world

print('hello world')     # This line prints Hello World on the screen

#Q2.Print your name

'''
Program idea:

Ask user: “Enter your name: ”

Print: “Hello, [name]!”
'''

name=input('Enter your name:')
print("hello",name,'!')
print()

#Q3.Simple arithmetic

'''
Program idea:

Ask user for 2 numbers

Print their sum, difference, product, and division
'''

num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))

print('sum:', num1+num2)
print('difference:', num1-num2)
print('product:', num1*num2)
print('division:', num1/num2)
print()

#Q4.Even or Odd     [Input a number, check if it’s even or odd.]

a=int(input('enter number:'))
if a%2==0:
    print('even number')
elif a%2!=0:
    print('odd number')
else :
    print('invalid number')
print()

#Q5.Greatest of 2 numbers   [Take 2 numbers as input and print which one is bigger.]

num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))

if num1 > num2:
    print("First number is bigger")
elif num2 > num1:
    print("Second number is bigger")
else:
    print("Both numbers are equal")

print()

#Q6.Simple loops

'''
Print numbers from 1 to 10 using a for loop.

Print numbers from 10 to 1 using a while loop.'''


for i in range(1,11):
    print(i)
print()


b=1
i=10
while b<=i:
    print(i)
    i-=1

#Q7.Sum of first N numbers

'''
Ask user for N

Print sum of 1 + 2 + … + N '''

n=int(input('enter:'))
b=str(n)
sum=0
for i in range (1,n+1):
    sum+=i
print(sum)



#Q8.List basics
'''
Create a list of numbers

Print all elements

Print sum of all elements'''

l=eval(input('enter list:'))
print(l)
sum=0
for i in l:
    sum+=i

print(sum)


#Q9.Simple string operations

'''
Take a string input

Print its length, uppercase, lowercase'''


s=eval(input('enter:'))
print(len(s))
print(s.upper())
print(s.lower())


#Q10.Simple conditions with strings

'''
Ask user for password

Print “Correct” if it matches, else “Wrong”'''


# Ask user for password
password = input("Enter password: ")

# Check if it matches
if password == "python123":
    print("Correct ✅")
else:
    print("Wrong ❌")


