#while condition:
# code block
i=0
while i<10:
    print(i)
    i+=1

#print the numbers from 9 to 27
i=9
while i<28:
    print(i)
    i+=1
#10 to 1
i=10
while i>1:
    print(i)
    i-=1
#print the squares of a number from 2 to 6
i=2
while i<=6:
    print("square of ",i, "is" ,i**2)
    i+= 1
#1 Table:
i=1
while i<=10:
    print("1 x ",i, "=",i)
    i += 1
#odd numbers from 0 to 20
i=1
while i<=20:
    print(i, "is an odd number")
    i +=2
#print sum of 25 numbers
i=1
total=0
while i<=25:
    total= total+i
    i+=1
    print(total)
#print factorial of 5
i=1
total=1
while i<=5:
    total=total*i
    i+=1
    print(total)
for i in range(0,11):
    if i%2!=0:
        pass
    else:
       print(i)
