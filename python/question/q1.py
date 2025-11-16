# for i in range (5):
#     print("sagar")
    
# evven or odd check 
# num = int(input("enter your number"))
# if num % 2 == 0:
#     print("your number is even")
# else:
#     print("odd")

#Sum of first 10 natural numbers

# total = 0 
# for i in range(1,11):
#      total +=i
# print("sum of the first 10 number is :", total)

# word = input("Enter your word to reverse it ")
# reverse = word[::-1]
# print("reversed word is :", reverse)

#FINDING THE LARGEST AND THE SMALLLEST NUNMBER

# a,b,c = 10,2,42
# print(max(a,b,c))
# print(min(a,b,c))

# Count vowels in a string

# word = input("enter your word :").lower()
# count = 0 
# for c in word:
#     if c in "aeiou":
#         count += 1
# print("vowel amount is :" , count)

#Factorial of a number
# number = int(input("enter your number to see the factorial number  : "))
# fact = 1
# for i in range (1, number+1):
#     fact *=i
# print(fact) 


#Check palindrome

# word = input("enter your word ")

# if word == word[::-1]:
#     print("yes bro you it")
# else:
#     print("no it is not")

#sum of digits of a number 

# number = (input("enter your number"))
# amount = 0
# for i in number :
#     amount += int(i)
# print ("sum of the number is ", amount)

# Multiplication table
# number = int(input("enter the number"))

# for i in range(1,11):
#     print(f"{number} x {i} = {i*number}"  ) 


#finding the maximum number in the list 
# nums = [3,24,5,2,1,5,2,5,2,52,6]
# print("max :", max(nums))

#Remove duplicates from a list

# nums = [1,2,3,4,2,4,2,4,2,4,2,5,8,5,36]
# unique = list(set(nums))
# print(unique)

# sen = "python is fun and python is easy"
# words = sen.split()
# print(words)
# feq ={}
# for w in words:
#     feq[w]= feq.get(w,0) +1
# print(feq)

# a = "listen"
# b = "silent"
# if sorted(a) == sorted(b):
#     print("Anagram")
# else:
#     print("Not anagram")

#finding the 2nd largest number

# nums=[1,2,31,3,2,3,4,24]
# new_list = list(set(nums))
# new_list.sort()
# snd_large= new_list[-2]
# print(snd_large)

# Find all prime numbers between 1–50

# for num in range(2, 51):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")

# or
for num in range(2, 51):
    if num%2==0:
        break
    else:
        print(num,end=" ")



    



