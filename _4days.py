def calcu(first, second, opera):
    resu_calcu = 0
    end_calcu = False
    error_calcu = False
    if opera == '+':
        resu_calcu = first + second
    elif opera == '-':
        resu_calcu = first - second
    elif opera == '*':
        resu_calcu = first * second
    elif opera == '/':
        resu_calcu = first / second
    elif opera == 'exit':
        end_calcu = True
    else:
        print("Error: Unsupported operator or invalid command.")
        error_calcu = True
    return resu_calcu, end_calcu, error_calcu





end = False
while end != True:
    error = False
    first_number = int(input("Choose a number:\n"))
    second_number = int(input("Choose another number:\n"))
    operation = input("Choose an operation:\n\tOpyions are: + , - , * or /.\n\tWrite 'exit' to finish.\n")
    
    result, end, error = calcu(first_number, second_number, operation)
    if error == True:
        continue
    if end == True:
        continue

    print(f"Result: {result}")