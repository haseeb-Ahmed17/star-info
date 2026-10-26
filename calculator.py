
# Simple Calculator with History

history = []

while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. View Calculation History")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "6":
        print("Calculator closed. Goodbye!")
        break

    elif choice == "5":
        print("\n===== CALCULATION HISTORY =====")

        if len(history) == 0:
            print("No calculations yet.")
        else:
            for calculation in history:
                print(calculation)

    elif choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                operator = "+"

            elif choice == "2":
                result = num1 - num2
                operator = "-"

            elif choice == "3":
                result = num1 * num2
                operator = "*"

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue

                result = num1 / num2
                operator = "/"

            calculation = f"{num1:g} {operator} {num2:g} = {result:g}"

            print("Result:", result)
            history.append(calculation)

        except ValueError:
            print("Invalid input! Please enter numbers.")

    else:
        print("Invalid choice! Please choose 1 to 6.")
