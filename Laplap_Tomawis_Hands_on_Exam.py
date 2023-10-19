print("Enter 1 for Decimal to Binary conversion \nEnter 2 for Decimal to Octal conversion \nEnter 3 for Decimal to Hexadecimal conversion \n")
number = int(input("Enter method number: "))

if number == 1:
    decimal = int(input("Enter a decimal number:"))
    print(format(decimal, "b"))
elif number == 2:
    decimal = int(input("Enter a decimal number:"))
    print(format(decimal, "o"))
elif number == 3:
    decimal = int(input("Enter a decimal number:"))
    print(format(decimal, "x"))
else:
    print("Invalid input. Please try again.")

