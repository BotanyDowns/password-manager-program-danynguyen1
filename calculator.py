# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")


        #this program calculates the fines for speeding ticket

def enterFine ():
    global totalFines

    validInput = False
    while validInput ==False:
        try:
            speedlimt = int(input("Enter Speed Limit :")) #local variables
            speed = int(input("Enter Speed :"))
            amountOver = speed - speedlimit

            if amountOver > 0:
                validInput = True

                totalFines += 630

                fines.append([name, amountOver]) #add name and amountOver to fines lists
            else:
                print("Error the speed must be a positive number and above the speed limit, enter again!")

        except:
                print("Error: Please enter umber values only")

#main routine
name = input("Enter driver name? :")
checkWarrant(name) #call checkWarrant function enter value name
enterFine() #call enterFine function
print("Fine for ", name, "is ",totalFines)
