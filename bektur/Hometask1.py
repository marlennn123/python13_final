num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
opperation = input("Enter the operator:")


if opperation == "+":
    print(num_1 + num_2)

elif opperation == "-":
     print(num_1 - num_2)

elif opperation == "*":
    print(num_1 * num_2)

elif opperation == "/":
    print(num_1 / num_2)

elif opperation == "**":
    print(num_1 ** num_2)

elif opperation == "//":
    print(num_1 // num_2)

elif opperation == "%":
    print(num_1 % num_2)

else:
    print("Error, the operator is written incorrectly")

