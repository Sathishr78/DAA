#1.first palindrome in array
A=["siri","lahari","madam","aka"]
for i in A:
    if(i==i[::-1]):
        break
print(i)
#2.number which are presented in list1 are in list2
n1=[4, 3, 2, 3, 1]
n2=[2, 2, 5, 2, 3, 6]
ans1=sum(i in n2 for i in n1)
ans2=sum(i in n1 for i in n2)
print(ans1,ans2)
# 3.square sum of the distinct values in nums[i..j]
n1 = [1, 2, 7,8]
sum= 0
for i in range(len(n1)):
    distinct = set()
    for j in range(i, len(n1)):
        distinct.add(n1[j])
        sum += len(distinct) ** 2
print(sum)
#4.how many no.of pairs in a list where 0<=i<j<n,n1[i]=n1[j],i*j%k
nums = [3,1,2,2,2,1,3]
k = 2
count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and (i * j) % k == 0:
            count += 1
print(count)
#5.Write a program FOR THE BELOW TEST CASES with least time complexity
n = [{1, 2, 3, 4, 5}, {7, 7, 7, 7, 7},{-10, 2, 3, -4, 5}]
for i in n:
    print(max(i))
#6.write a program for sorting try test cases Input: [],Input: [5],Input: [3, 3, 3, 3, 3]
#case3
n = [3,3,3,3,3,3]
s= sorted(n)
maxe = s[-1]
print( s)
print( maxe)
#7.remove duplicate from the list
list1 = [1, 2, 2, 3, 4, 4, 5]
list2= []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
#8.bubble sort
a= [64, 34, 25, 12, 22, 11, 90]
n = len(a)
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
#9.search a number by using binary search
a= [1, 2, 3, 4, 5]
x = 3
l, r = 0, len(a) - 1
while l <= r:
    m = (l + r) // 2
    if a[m] == x:
        print("Found")
        break
    elif a[m] < x:
        l = m + 1
    else:
        r = m - 1
else:
    print("Not Found")
#10.asending order without using built-in-function
a = [5, 2, 9, 1, 5, 6]
n = len(a)
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1],a[j]
print(a)






    
