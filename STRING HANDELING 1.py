#11. Count uppercase and lowercase letters.

a="beautyBEAUTIFUL"
count_uppercase=0
count_lowercase=0
for i in a:
    if "A" <=i<="Z":
        count_uppercase+=1
    elif "a" <=i<="z":
        count_lowercase+=1
    else:
        print("invalid")
print("count uppercase in a string:",count_uppercase)      #9
print("count lowercase in a string:",count_lowercase)      #6
print()
#12. Count digits in a string.

a = "gfb342gh54"
count_digit = 0

for i in a:
    if "0" <= i <= "9":  
        count_digit += 1

print("count digits in a string:",count_digit)  #5
print()

#13. Count spaces in a string.

a='india     is    developing   country'
count=0
for i in range(len(a)):
    if a[i]==' ':
        count+=1
print("count space in a string: ",count)
print()    

#14. Check if string contains only digits.
a = "1243546576895"

for i in a:
    if not ("0" <= i <= "9"):   
        print("String does not contain only digits")
        break
else:
    print("String contains only digits")
print()

#15. Reverse words in a sentence.

a = "This place is very beautiful"
b = a.split()
res = ""

for i in range(len(b)-1, -1, -1):   # words ke liye
    res += b[i] + " "

print(res.strip())
print()


#16. Find first non-repeating character.

a = "eeeewerrr"

for i in a:
    if a.count(i) == 1: 
        print("First non-repeating character:", i)
        break        
print()

#17. Find most frequent character.

a = "eeeewerrr"

max_count = 0
most_freq = ""

for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        most_freq = i

print("Most frequent character is:", most_freq)
print("Frequency:", max_count)
print()


#18. Replace first word with another.

a = "This place is very beautiful"

words = a.split()       
words[0] = "That"      
res = " ".join(words)  

print(res)
print()

#19. Find duplicate words in a string.

a = "this place is very very beautiful place"

words = a.split()
duplicates = []

for i in words:
    count = 0
    for j in words:
        if i == j:
            count += 1
    if count > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate words:", duplicates)
print()

#20. Remove duplicate words from a string.

a = "this place is very very beautiful place"

words = a.split()
unique = []

for i in words:
    if i not in unique:   
        unique.append(i)

res = " ".join(unique)
print(res)
