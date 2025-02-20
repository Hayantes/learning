print("Hello choose your number you want to divide and choose it's divisor !")
number_divide  = int(input("Number you want to divide: "))
number_divisor  = int(input("Number divisor: "))
if number_divisor > number_divide:
    print("Please remember that divide number should be more than divide number !")
    exit()
if number_divisor == number_divide:
    print("You know basic math and you know your answer...")
    exit()
result = number_divide//number_divisor
if result % 2 == 1:
    print(f"Your result is " + str(result) + " and it's odd number")
elif result % 2 == 0 and result % 4 == 0:
    print(f"Your result is " + str(result) + " and is both even and can be divided on 4 ? You probabl Guido Mista ")
else:
    print(f"Your result is " + str(result) + " and it's even number")