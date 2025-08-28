
#11. Find second smallest element.
a=[10,20,30,40,50,60]
print(a)                            #[10, 20, 30, 40, 50, 60]
a.remove(min(a))
print("second smallest:-",min(a))   #second smallest:- 20
print()
    
#12. Merge two lists.
a=[1,2,3]
b=[4,5,6]

mrge=a+b
print(mrge)                         #[1, 2, 3, 4, 5, 6]

#"Merge two lists alternately"
merge=[]
for i,j in zip(a,b):
    merge.append(i)
    merge.append(j)
print(merge)                        #[1, 4, 2, 5, 3, 6]
print()
#13. Find common elements in two lists.

a = [1, 2, 3,4,4, 5]
b = [4, 5, 6, 7]


#i.using control statement
common=[]
for i in a:
    for j in b:
        if i==j:
            if i not in common:
                common.append(i)
print("Common using  control statement: ",common)    #Common using  control statement:  [4, 5]

# ii. Using set intersection
common1 = list(set(a) & set(b))            
print("Common using set:", common1)         #Common using set: [4, 5]
print()


#14. Find unique elements in a list.

a = [1,2,3,4]
b = [3,4,5,6]

union= set(a).union(set(b))
print(list(union))          #[1, 2, 3, 4, 5, 6]      
print()


#15. Check if list is sorted or not.
a = [1, 2, 3, 4, 5]

if a == sorted(a):
    print("List is sorted in ascending order")  #List is sorted in ascending order
elif a == sorted(a, reverse=True):
    print("List is sorted in descending order")
else:
    print("List is not sorted")


#16. Rotate list elements.
a = [1, 2, 3, 4, 5]
k = 2  #how many times rotate

# right rotation
rotated_right = a[-k:] + a[:-k]
print("Right Rotate:", rotated_right)           #Right Rotate: [4, 5, 1, 2, 3]

# left rotation
rotated_left = a[k:] + a[:k]
print("Left Rotate:", rotated_left)             #Left Rotate: [3, 4, 5, 1, 2]


#17. Replace negative numbers with 0.
a=[1,2,-3,4,-5,6,7,-8,9,-10]

for i in range (len (a)):
    if a[i]<0:
        a[i]=0
print(a)        #[1, 2, 0, 4, 0, 6, 7, 0, 9, 0]
print()
        


#18. Separate even and odd numbers from a list.
a=[10,20,3,40,5,60,7,80,9,100]
even=[]
odd=[]
for i in range(len(a)):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
print("even number list : ",even)       #even number list :  [10, 20, 40, 60, 80, 100]
print("odd number list",odd)            #odd number list [3, 5, 7, 9]
print()       

#19. Find sum of even numbers in a list.
a=[10,20,3,40,5,60,7,80,9,100]
even=[]
s=0
for i in range(len(a)):
    if a[i]%2==0:
        even.append(a[i])
for i in even:
    s+=i
    
print("even number list : ",even)  #even number list :  [10, 20, 40, 60, 80, 100]
print("sum of even number: ",s)   #sum of even number:  310
print()

  

#20. Find product of all elements in a list.

a=[1,2,3,4,5,6,7,8,9,10]
product=1
for i in range(len(a)):
    product*=a[i]
print(product)              #3628800
