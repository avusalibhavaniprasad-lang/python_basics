# ceating an array:
import array as arr
Numbers = arr.array('i',[1,2,3,4,5])
print(Numbers)
print(type(Numbers))

Numbers.append(6)
print(Numbers)

Numbers.insert(2,5)
print(Numbers)

Numbers.extend([7,8])
print(Numbers)

Numbers.remove(2,5)
print(Numbers)

Numbers.pop(3)
print(Numbers)

# looping through arrays:
for i in Numbers:
    print(i)
