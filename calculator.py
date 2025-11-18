def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit")
    
    while True:
        try:
            # Get user input
            expression = input("Enter expression (e.g., 2 + 3): ").strip()
            
            if expression.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Split the expression into parts
            parts = expression.split()
            if len(parts) != 3:
                print("Invalid format. Use: number operator number")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            # Perform calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Use +, -, *, or /")
                continue
            
            print(f"Result: {result}")
        
        except ValueError:
            print("Invalid input. Please enter numbers and a valid operator.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
calculator()
