num1 = 1
num2 = 1

while num1 != "0" or num2 != "0":
    num1 = int(input("Type 1 Whole Number"))
    num2 = int(input("Type a 2nd Whole Number"))
    if num1 > num2:
        print(num1)
    elif num2 > num1:
        print(num2)
    else:
        print("Numbers are equal")
