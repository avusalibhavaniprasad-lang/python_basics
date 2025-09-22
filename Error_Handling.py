# ZeroDivisionError:
try:
    nume = int(input("Enter the numarator: "))
    deno = int(input("Enter the denominator: "))
    divi = nume/deno
    print(divi)
except ZeroDivisionError:
    print("error")
    print("invalid")

# ValueError:
try:
    rollno = int(input("Enter your rollno:"))
except ValueError:
    print("Error")
  
# type error:
try:
    sum = 28+5
    print(sum)
except TypeError:
    print("error")

# index error:
try:
    Dict = {"name":"sarayu","RollNo":"J7"}
    print[Dict{"age"}]
except IndexError:
    print("Error:the given index is not in the list")
    