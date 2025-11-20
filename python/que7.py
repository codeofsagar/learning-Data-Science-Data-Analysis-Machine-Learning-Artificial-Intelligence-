user_input = int(input("Hello user give me your input "))

if user_input % 2 == 0 :
    print(f"your number {user_input} is even")
elif user_input % 2 != 0 :
    print(f"your number {user_input} is odd")
else :
    print("you have given wrong input")