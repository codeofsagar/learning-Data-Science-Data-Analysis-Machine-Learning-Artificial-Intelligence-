word= input("give me your word")
lst = list(word)
lst[0]="J"
lst[-1]="X"
ret_word="".join(lst)
print(ret_word)