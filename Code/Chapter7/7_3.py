number = input("Enter a number, and I'll judge if it's a integer multiples of 10. ")
number = int(number)

if number % 10 == 0:
    print(f"\n The number {number} is a ingteger multiples of 10.")
else:
    print(f"\n The number {number} is not a ingteger multiples of 10.")