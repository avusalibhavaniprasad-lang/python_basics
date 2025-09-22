list1 = [10,20,30,40,50]
list2 = [10.1,20.2,30.3,40.4,50.5]
list3 = ["apple","banana","mango"]
list4 = [True,False,True,False]
list5 = [10,10.1,"apple",True,"False"]
print(list5)
# list1 = [10,20,30,40,50]
print(list1[0]) 
print(list1[1]) 
print(list1[2]) 
print(list1[3])
print(list1[-1]) 
print(list1[-2]) 
print(list1[-3]) 
print(list1[-4]) 
 

kalkicast = ["prabhas","ssr","vijay","amitha b"]
# add a new role for prabhas owner
kalkicast.append("bhramanadham")
print(kalkicast)
kalkicast.remove("ssr")
print(kalkicast)
kalkicast.clear()
print(kalkicast)
a = [2,4,6,8,10,12,14]
#idx  0 1 2 3 4 5 6 7
if 2 in a:
    print("yes item is present in the list")

print(3 not in a)  

st = [25,18,5,28,8,14,15,7,48,67,99]
# reverse = 99,67,48,7,15,14,8,28,5,18,25
st.reverse()
print(st)
st = [25,18,5,28,8,14,15,7,48,67,99]
#ao = 5,7,8,14,15,18,25,28,48,67,99
st.sort()
#do = 99,67,48,28,25,18,15,14,8,7,5
# st.reverse()
print(st)

frd1 = ["A","C","B","D","C","C","B","A","B","D"]
frd2 = frd1.copy()
print(frd2)
st = [25,18,5,28,8,14,15,7,48,67,99]
print(len(st)) # 11                                                

cars = ["swift","innova","indigo","santro","thar"]
#index   0        1        2       3         4
l = len(cars) #5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
for i in range(0,4): # 0 1 2 3 4
    print(cars[i]) # 1 2 3 4

# convert ["p","y","a","b","h","i"] to python
b = ["p","y","a","b","h","i"]
word = ""
for i in b:
    word = word + i
print(word)

# find the maximum and minimum number from list without using max() and min().
numbers = [218,227,265,219,8,229,256,1,5,9,12]
max_n = numbers[0]
min_n = numbers[0]
for i in numbers: #i = 59,200,8,5,219,229,227,54,68,84,58
    if i > max_n: # 227 > 229
        max_n = i
if i < min_n: # 227 < 5
    min_n = i  
# searching for an element in a list
P_names = ["modi","revanth rddy","PSPK","YSR"] 
searching_names = input("enter the name to be search in the list:") # YSR Ktr
found = False
i = len(P_names) # 1 = 4
for i in range(1): # 0 1 2 3
    if searching_names == P_names[i]:
        found = True 
         
if found:
   print("yes")
else:
    print("No")  

# Count even and odd numbers
a = [2,5,99,7,6,23,44,48,52,77,62,61] # Even = 6 odd = 6
evn_cnt = 0
odd_cnt = 0
for i in a:
    if i%2==0:
        evn_cnt +=1
    else:
        odd_cnt += 1 
print("Number of even numbers in the list:",evn_cnt)
print("Number of odd numbers in the list:",odd_cnt)

# Reversing a list without reverse
a = [2,5,99,7,6,23,44,48,52,77,62,61] 
#i   0 1  2 3 4  5  6  7  8  9 10 11 
l  = len(a) # 12
r_list = []
for i in range(l-1,-1,-1):
    r_list.append(a[i])
print(r_list)

# Removing all negative numbers using loop  
# o = 5,6,23,48,52,,62
a = [-2,5,-99,-7,6,23,-44,48,52,-77,62,-61]
b = []
p_list = []
for i in a:  
    if i > 0:
        p_list.append(i)
print(p_list)

# Multiply each element with 2 in the list
p_list = []
for i in a:
    b.append(i*2)
    print(b)

list1 = [1,2,3,4,5,6,7,8,9,10]  
seperate = ("even")
seperate = ("odd")
print("the even numbers and odd numbers from list1")
        
        


 





















































































































































































































































































































































































































































































































































































































































































































































































































































































































