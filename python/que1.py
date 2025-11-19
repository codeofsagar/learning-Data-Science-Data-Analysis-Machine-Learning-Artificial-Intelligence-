first_inp = int(input("give me your first number : "))
sec_inp = int(input("give me your secound number : "))
third_inp = int(input("give me your third number : "))

lst = []
lst.append(first_inp)
lst.append(sec_inp)
lst.append(third_inp)

lst.sort()
print(lst[1])
