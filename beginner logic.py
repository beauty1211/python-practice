#1. Find factorial of a number.
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)  #output: 120

#2. Find sum of digits of a number.
n=5
sum=0
for i in range(0,n+1):
    sum+=i
print(sum)  #output:- 15

#3. Reverse a number.
a=10
for i in range (10,0,-1):
    print(i,end=' ')    #output :- 10 9 8 7 6 5 4 3 2 1 
print()

#4. Check if a number is palindrome.

a='121'
if a[::-1]==a:
    
    print('its palindrome') #output: its palindrome


#5. Generate Fibonacci series up to n.
'''
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
and so on...
'''
    
n = 10
a, b = 0, 1
for i in range(n + 1):
    print(a ,end=' ')
    a, b = b, a + b
print()
print() 
#----DRY RUN----
'''

Initial values:

- n = 10
- a = 0
- b = 1

Iteration 1:

- i = 0
- print(a) => 0
- a, b = b, a + b => a = 1, b = 0 + 1 = 1

Iteration 2:

- i = 1
- print(a) => 1
- a, b = b, a + b => a = 1, b = 1 + 1 = 2

Iteration 3:

- i = 2
- print(a) => 1
- a, b = b, a + b => a = 2, b = 1 + 2 = 3

Iteration 4:

- i = 3
- print(a) => 2
- a, b = b, a + b => a = 3, b = 2 + 3 = 5

Iteration 5:

- i = 4
- print(a) => 3
- a, b = b, a + b => a = 5, b = 3 + 5 = 8

Iteration 6:

- i = 5
- print(a) => 5
- a, b = b, a + b => a = 8, b = 5 + 8 = 13

Iteration 7:

- i = 6
- print(a) => 8
- a, b = b, a + b => a = 13, b = 8 + 13 = 21

Iteration 8:

- i = 7
- print(a) => 13
- a, b = b, a + b => a = 21, b = 13 + 21 = 34

Iteration 9:

- i = 8
- print(a) => 21
- a, b = b, a + b => a = 34, b = 21 + 34 = 55

Iteration 10:

- i = 9
- print(a) => 34
- a, b = b, a + b => a = 55, b = 34 + 55 = 89

Iteration 11:

- i = 10
- print(a) => 55
- a, b = b, a + b => a = 89, b = 55 + 89 = 144

Output:

0 1 1 2 3 5 8 13 21 34 55

The program prints the first 11 numbers in the Fibonacci series.

'''


#6. Find LCM of two numbers.
a=4
b=6

greater =max(a,b)
while True:
    if (greater% a==0) and (greater %b==0):
        lcm = greater
        break
    greater +=1
print("LCM of", a, "and", b, "is:", lcm)

#-----DRY RUN ------

'''
Dry Run (a=4, b=6)

Check which is greater

a=4, b=6

a > b ❌ false

so greater = b = 6

Start while True loop

greater = 6

condition: (6 % 4 == 0) and (6 % 6 == 0)
→ 6 % 4 = 2 ❌ not 0
→ condition false

so greater = 6 + 1 = 7

Next iteration

greater = 7

(7 % 4 == 0) and (7 % 6 == 0)
→ 7 % 4 = 3 ❌
→ condition false

greater = 8

Next iteration

greater = 8

(8 % 4 == 0) and (8 % 6 == 0)
→ 8 % 4 = 0 ✅
→ 8 % 6 = 2 ❌
→ false

greater = 9

Next iteration

greater = 9

(9 % 4 == 0) and (9 % 6 == 0)
→ 9 % 4 = 1 ❌
→ false

greater = 10

Next iteration

greater = 10

(10 % 4 == 0) and (10 % 6 == 0)
→ 10 % 4 = 2 ❌
→ false

greater = 11

Next iteration

greater = 11

(11 % 4 == 0) and (11 % 6 == 0)
→ ❌

greater = 12

Next iteration

greater = 12

(12 % 4 == 0) and (12 % 6 == 0)
→ 12 % 4 = 0 ✅
→ 12 % 6 = 0 ✅
→ condition ✅ true

👉 so lcm = 12
👉 break loop
'''




#7. Find HCF of two numbers.

a = 4
b = 6


smaller = min(a, b)

hcf = 1  # default HCF = 1

for i in range(1, smaller + 1):
    if (a % i == 0) and (b % i == 0): 
        hcf = i 


print("HCF of", a, "and", b, "is:", hcf)
print()

#----DRY RUN----
'''
🔎 Dry Run (a = 4, b = 6)

👉 smaller = 4
👉 loop chalega 1 → 4

i = 1 → (4 % 1 == 0) and (6 % 1 == 0) ✅ → hcf = 1

i = 2 → (4 % 2 == 0) and (6 % 2 == 0) ✅ → hcf = 2

i = 3 → (4 % 3 != 0) ❌ → skip

i = 4 → (6 % 4 != 0) ❌ → skip

✅ Final hcf = 2

'''

#8. Find power of a number without using **.


base = int(input("Enter the base number: "))   # Example: 2
exp = int(input("Enter the exponent: "))       # Example: 3

result = 1
for i in range(exp):
    result = result * base   # multiply base exp times

print(base, "raised to the power", exp, "is:", result)

#----DRY RUN----

'''
Dry run line by line

Initialization

base = 4

exp = 3

result = 1 (shuru me)

Loop start → for i in range(3) → i = 0, 1, 2

🔹 Iteration 1 (i = 0):

result = result * base

result = 1 * 4

result = 4

🔹 Iteration 2 (i = 1):

result = result * base

result = 4 * 4

result = 16

🔹 Iteration 3 (i = 2):

result = result * base

result = 16 * 4

result = 64

Loop khatam (kyunki i = 0,1,2 tak hi chala)

Final result = 64


✅ Output: 4 raised to the power 3 is: 64
'''

#9. Count digits in a number.
a=1234567
b=str(a)
print("Total digits:",len(b))
print()

#without string

num = 4567
count = 0

while num > 0:
    num = num // 10   # ek ek digit remove hota hai
    count = count + 1

print("Total digits:", count)
print()

#-----Dry run-----
'''
Dry run karein to:

4567 → 456 (count=1)

456 → 45 (count=2)

45 → 4 (count=3)

4 → 0 (count=4)

Final answer = 4
'''

#10. Find average of 5 numbers.

a=90
b=75
c=80
d=89
e=89

avg=(a+b+c+d+e)/5
print(avg)
print()

#11. Find greatest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print("Greatest is:", greatest)




#another way
print("Greatest is:", max(a, b, c))


#12. Find smallest of three numbers.



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("Smallest is:", smallest)

#another way :-
print("Smallest is:", min(a, b, c))


#13. Check leap year.

y=2024

if y%4==0 or y%100!=0 or y%400==0:
    print('leap year')
else:
    print('not leap year')
print()

#14. Find ASCII value of a character.
a='A'
print(ord(a)) #65

#15. Convert string to uppercase without .upper().
s = "Beauty"
result = ""

for ch in s:
    if 'a' <= ch <= 'z':  
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)   # BEAUTY


#16. Convert string to lowercase without .lower().
s = "BEAUTY"
result = ""

for ch in s:
    if 'A' <= ch <= 'Z':  
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)   # beauty
5

#17. Reverse a string.

a = 'beauty'
r = ''
for i in range(len(a)-1, -1, -1):  # start = last index, end = -1 (exclusive), step = -1
    r += a[i]
print(r)


#18. Count characters in a string.

a = 'beauty'
count = 0

for ch in a:   
    if ch in 'aeiouAEIOU':  
        count += 1           

print("Number of vowels:", count)

#20. Count consonants in a string.

a = 'beauty'
count = 0

for ch in a:   
    if ch not in 'aeiouAEIOU':   
        count += 1           

print("Number of consonants:", count)


