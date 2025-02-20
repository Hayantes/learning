print("Hello, choose your number !")
user_number  = int(input())
if user_number % 2  == 1:
    print(f"Your number is " + str(user_number) + " and it's  odd !")
elif user_number % 2 == 0 and user_number % 4 == 0:
    print(f"Your number is both even and can be divided on 4 ? You probabl Guido Mista ")
else:
    print(f"Your number is " + str(user_number) + " and it's even !")