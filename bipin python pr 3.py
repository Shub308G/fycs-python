marks = float(input("enter your marks:"))

if marks >=101:
    print("invalid input")

elif marks >= 90:
    print("grade A")

elif marks >=75:
    print("grade B")

elif marks >= 50:
    print("grade C")

elif marks >=35:
    print("grade D")

else:
    print("fail")

for i in range(1,11):
    print(f"2 * {i} = {2*i}")
    print(f"3 * {i} = {3*i}")
    print(f"4 * {i} = {4*i}")



