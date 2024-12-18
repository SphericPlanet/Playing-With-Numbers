number = int(input("Enter Your Number: "))

original_Number = number
reversed_Number = 0

while number > 0:
    digit = number % 10
    reversed_Number = reversed_Number * 10 + digit

    number //=10

if original_Number == reversed_Number:
    print(f"{original_Number} is a palindrome.")
else:
    print(f"{original_Number} is not a palindrome.")

