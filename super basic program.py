#1. Print "Hello World".
print('hello world')  #output:- hello world  
print()

#2. Print your name.

name=input('enter your name:')     #output:- beauti
print(name)
print()


#3. Print numbers from 1 to 10 using loop.

for i in range(1,11):
    print(i ,end=' ') #output: 1 2 3 4 5 6 7 8 9 10
print()



#4. Print even numbers between 1–20.
i=1
while i<=20:
    print(i,end=' ')  # output: 2 4 6 8 10 12 14 16 18 20
    i+=2
print()   


#5. Print odd numbers between 1–20.
i=1
while i<=20:
    print(i,end=' ')    #output: 1 3 5 7 9 11 13 15 17 19 
    i+=2
print() 


#6. Find sum of first 10 natural numbers.
a=10
sum=0
i=1
while i<=10:
    sum+=i
    i+=1
print(sum) #output:- 55
print()

#7. Print multiplication table of 5.

mul=5
i=1
while i<=10:
    print(a*i ,end=' ') #output:- 10 20 30 40 50 60 70 80 90 100
    i+=1
print()

#8. Take user input and print it.
a=input('enter: ')      #output: enter: hello
print(a)               #output:  hello
print()

#9. Swap two numbers (with third variable).
a=10
b=20
c=0
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap numbers using a third variable
c = a
a = b
b = c

print("After swapping:")
print("a =", a)
print("b =", b)
print()

#OUTPUT:-

'''
Before swapping:
a = 10
b = 20
After swapping:
a = 20
b = 10
'''

#10. Swap two numbers (without third variable).

a = 10
b = 20
print("Before swapping:")
print("a =", a)
print("b =", b)
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
print()

#OUTPUT:-
'''
Before swapping:
a = 10
b = 20
After swapping:
a = 20
b = 10
'''

#11. Find square of a number.
a=10
print(a**2)
print()     #OUTPUT:-100



#12. Find cube of a number.
a=10
print(a**3)
print()     #OUTPUT:-1000

#13. Find area of a rectangle.
l=10
b=5
area=l*b
print('area of rectangle: ',area)  #OUTPUT:- area of rectangle:  50
print()

#14. Find area of a circle.
r=5
p=3.14
area=  p* r*r
print('area of circle: ',area)   #OUTPUT:- area of circle:  78.5
print()

#15. Convert Celsius to Fahrenheit.
c=5
f=(c*9/5)+32
print('Fahrenheit: ',f)     #OUTPUT:- Fahrenheit:  41.0
print()

#16. Convert Fahrenheit to Celsius.
f=41
c=(f-32)*5/9

print('Celsius:' ,c)  #OUTPUT:-Celsius: 5.0
print()

#17. Find maximum of two numbers.

num1 = 10
num2 = 20
print(max(num1, num2)) # Output: 20
print()

#18. Find minimum of two numbers.
num1 = 10
num2 = 20
print(min(num1, num2))  #Output:10
print()

#19. Check whether a number is positive or negative.
a=10
if a>0:
    print('positive number')
else:
    print('negative number')
#OUTPUT:- positive number
print()

#20. Check whether a number is even or odd.

a=10
if a%2==0:
    print('even number')
else:
    print('odd number')
print()

#OUTPUT:- even number

