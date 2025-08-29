#1. Check if string is palindrome.
a='madam'
if a[::-1]==a:
    print('palindrome')         #palindrome
print()


#another way (without slicing)
res=''
for i in range(len(a)-1,-1,-1):
    res+=a[i]
    i-=1
if res==a:
    print("string is palindrome")
else:
    print("string is not palindrome")
print() 

#2. Find length of string (without len()).
b='aman'
l=0
for i in b:
    l+=1
print("length of string: ",l)       #length of string:  4
print()

#3. Count words in a string.
a="This place is very beautiful"
c=a.split()
print(len(c))
print()
#4. Find longest word in a string.

a="This place is very beautiful"
c=a.split()
longest=max(c,key=len)

print("longest word in a string: ",longest)
print()

#5. Replace vowels with *.

a = "This place is very beautiful"
result = ""

for i in a:
    if i in "aeiouAEIOU":
        result += "*"
    else:
        result += i

print(result)
print()

#6. Find substring in a string.

a = "This place is very beautiful"
sub = "very"

if sub in a:
    print("Substring found!")
else:
    print("Substring not found!")
print()

#7. Remove all spaces from a string.

a = "This place is very beautiful"
result = ""

for i in a:
    if i !=' ' :
        result += i

print(result)
print()


#8. Remove all digits from a string.
a = "This12345 place23456 is1323456 ve14254365ry beautiful"
res=''
for i in a:
    if not i.isdigit():
        res+=i
print(res)


#9. Remove all special characters from a string.

a = "Th!s pl@ce i$ v#ry be@utiful 2025!!!"
result = ""

for ch in a:
    ascii_val = ord(ch)   # character ka ASCII nikalna
    if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122) or (48 <= ascii_val <= 57) or ascii_val == 32:
        result += ch    # sirf alphabets, numbers, space rakho

print("String after removing special characters:", result)
print()

#10. Convert string to title case.

a = "this place is very beautiful"
result = ""
word = ""

for i in range(len(a)):
    if a[i] != " ":           # word banana
        word += a[i]
    else:
        # pehle character ko uppercase aur baaki lowercase
        result += word[0].upper() + word[1:].lower() + " "
        word = ""             # reset word

# last word bhi add karna hoga
if word:
    result += word[0].upper() + word[1:].lower()

print("Title case string:", result)
print()


