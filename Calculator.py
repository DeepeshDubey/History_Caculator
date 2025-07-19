HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("NO HISTORY FOUND!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')  # use 'w' not 'W'
    file.close()
    print('HISTORY CLEARED')

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('INVALID INPUT. USE FORMAT: NUMBER OPERATOR NUMBER (e.g 8 + 8)')
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print('CANNOT DIVIDE BY ZERO')
            return
        result = num1 / num2
    else:
        print('INVALID OPERATOR, USE ONLY + - * /')
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)


def main():
    print('------SIMPLE CALCULATOR (TYPE HISTORY, CLEAR OR EXIT)------')
    while True:
        user_input = input("ENTER CALCULATION (+ - * /) OR COMMAND (HISTORY, CLEAR OR EXIT): ")

        if user_input.lower() == 'exit':
            print('Maa chudaoo')
            break
        elif user_input.lower() == 'history':
            show_history()
        elif user_input.lower() == 'clear':
            clear_history()
        else:
            calculator(user_input)

main()
