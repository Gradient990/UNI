tocontinueorfinish = 'y'
result = None
while tocontinueorfinish == 'y':
    x = float(input('First number: '))
    y = float(input('Second number: '))
    operation = input('Operation: ')
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        if y == 0:
            print("Divide by 0")
        elif y != 0:
            result = x / y
    elif operation == '//':
        floattoint = input("Do you want make your digit from float format to int format?[y/n]: ")
        if floattoint == 'y':
            result = x // y
        elif floattoint == 'n':
            tocontinueorfinish = 'y'
    elif operation == '**':
        result = x ** y

    if result is not None:
        print("Result: ", result)
        if result < 0:
            module = input("Do you want to make a module[y/n]: ")
            if module == 'y':
                module = abs(result)
                print(abs(result))
            else:
                print(result)

    else:
        print("No equals")
    tocontinueorfinish = input("Press 'y' to continue or 'n' to finish: ")

if tocontinueorfinish == 'n':
    print("See you later")
