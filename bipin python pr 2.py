a = 25
b = 15

print(a + b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

num = int(input("enter a number"))

if num % 2==0:
     print("even number")
     
else:
    print("odd number")
num= int(input("enter a number"))

if num <=1:
    print("neither prime nor composite")
elif num == 2:
    print("prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print("composite number")
            break
    else:
        print("prime number")

for i in range(1,11):
    print(*f"2x{i} = {2*i}")
