#Question 5: Reverse a number

#SOL-1
#USING ARITHMETIC
num = int(input("Enter the number"))
reverse = 0 

while num!=0:
    digit = num % 10
    reverse = reverse *10 + digit
    num //=10
    
print("reversed number is " , reverse)
 