# Stack using list
stack = []
# Function to push an element
def push():
    x = int(input("Enter element to push: "))
    stack.append(x)
    print(x, "pushed into stack")
# Function to pop an element
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Popped element:", stack.pop())
# Function to check empty stack
def is_empty():
    if len(stack) == 0:
        return True
    else:
        return False
# Function to display stack
def display():
    if is_empty():
        print("Stack is empty")
    else:
        print("Stack elements:", stack)
# Function to evaluate RPN expression
def evaluate_rpn():
    exp = input("Enter RPN Expression: ")
    temp = []
    for item in exp.split():
        if item.isdigit():
            temp.append(int(item))
        else:
            a = temp.pop()
            b = temp.pop()
            if item == '+':
                temp.append(b + a)
            elif item == '-':
                temp.append(b - a)
            elif item == '*':
                temp.append(b * a)
            elif item == '/':
                temp.append(b / a)
    print("Result:", temp.pop())
# Main menu
while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Evaluate RPN")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        evaluate_rpn()
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Invalid choice")