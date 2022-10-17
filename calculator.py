sum = 0

while(1):
    try:
        var = input("Enter the price = ")
        if var != "q":
            sum = sum + int(var)
            print(f"your toatal is = {sum}" )
        else:
            print(f"Your total price is {sum}. \nthank you for shopping with us.Please come again.")
            break
    except Exception as a:
        print("please enter a valid input.")
