#1. Print all elements of a list.
a=[10,'abc',10.4,45+5j]
for i in a:
    print(i)   #[10,'abc',10.4,45+5j]
print()

#2. Find sum of list elements.
s=[10,20,30]
summ=0
for i in range(len(s)):
    summ+=s[i]
print("sum of list element:",summ)   #60
print()

#another way
s = [10, 20, 30,40]
print("sum of list element:",sum(s))   # Output: 100
print()


#3. Find maximum element in a list.
s = [10, 20, 30,40]
print("maximum element:",max(s))  #40
print()

#4. Find minimum element in a list.
s = [10, 20, 30,40]
print("minimum element:",min(s))    #10
print()

#5. Find average of list elements.
s1 = [10, 20, 30,40]
s=0
for i in range(len(s1)):
    s+=s1[i]
print("average:",s/len(s1))     #25.0
print()

#6. Print list in reverse order.
a=['aman','suman','beauty']
r=[]
for i in range (len(a)-1,-1,-1):   
    r.append(a[i])
print(r)             #['beauty','suman','aman']
print()

#7. Sort list without using sort().
a = [5, 2, 8, 1, 3]
sl=[]
while a:
    mini= min(a)
    sl.append(mini)
    a.remove(mini)
print()   

print("Sorted list:", sl)   #[1, 2, 3, 5, 8]
print()
'''
s=[5, 2, 8, 1, 3]
print(sorted(s))        #output :- [1, 2, 3, 5, 8]
'''

#8. Remove duplicates from a list.

d=[1,1,2,2,3,3,4,4,5,5]

b=[]
for i in d:
    if i not in b :
        b.append(i)
    
print(b)    #[1,2,3,4,5]
print()

#9. Count frequency of each element.
a = [1, 2, 2, 3, 3, 3, 4, 4, 5]

freq = {}

for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)         #{1: 1, 2: 2, 3: 3, 4: 2, 5: 1}
print()

#10. Find second largest element.
a = [10, 20, 4, 45, 99]


largest=max(a)  #99

a.remove(largest)   #removing 99 and output is : [10, 20, 4, 45]
print("list after removing largest element: ",a)
second_largest=max(a)  #45
print("2nd largest:",second_largest )  #printing 45
print()


#another way
a=[10,20,70,30,80]
a.sort()   # ascending order
print("Second Largest:", a[-2])  #70














