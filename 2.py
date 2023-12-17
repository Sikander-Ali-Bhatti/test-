def factorial(num):
    if num < 0:
        print("Factorial is undefined for negative numbers.")
    else:
        result = 1
        while num > 0:
            result *= num
            num -= 1
        print(f"The factorial is: {result}")
user_input = int(input("Enter a number: "))
factorial(user_input)


