import random
from hangman_words import word_list
from hangman_art import stages,logo
# word_list = ["aardvark", "baboon", "camel"]

li=list(random.choice(word_list))
lis=[]
extra=7
life=7
user_answer=[]
for items in li:
    user_answer.append("_")
    lis.append("0")
print(user_answer) 
# print(lis)
print(logo)
while life>0:
    user=input("Enter a word")
    if(li.count(user)>0):
      user_answer[li.index(user)]=user
      li[li.index(user)]="0"
      print(user_answer)
      # print(lis)
      if(lis==li):
        print("You won")
        break
    else:
      print(user_answer)
      print(stages[6-extra])
      extra+=1
      life-=1
      print(f"life : {life}")
      if(life==0):
        print("You lost")
        break