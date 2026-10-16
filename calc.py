a = 10
b = 6

choice = input("Choose operation (+, -, *, /): ")

if choice == "+":
    print("Addition =", a + b)
elif choice == "-":
    print("Subtraction =", a - b)
elif choice == "*":
    print("Multiplication =", a * b)
elif choice == "/":
    print("Division =", a / b)
else:
    print("Invalid choice")
