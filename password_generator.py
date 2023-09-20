import random
Length=int(input("Enter the length of a Password "))
Input=int(input("Press 1 if you want to get a password in which only alphabets\nPress 2 if you want to get a password in which only digits\nPress 3 If you want to get a password in which both alphabets,digits and special characters "))
if Input==1:
 Password=''
 a=0
 while a < Length:
  character=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  choice=random.choice(character)
  Password+=choice
  a+=1
 print(Password)
elif Input==2:
 Password=''
 a=0
 while a < Length:
  choice=random.randint(1,9)
  Password+=str(choice)
  a+=1
 print(Password)
elif Input==3:
 Password=''
 while len(Password) < Length:
  character=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  choice1=random.choice(character)
  Password+=choice1
  special_character=["!","@","#","$","%","^","&","*",">","<","?"]
  choice2=random.choice(special_character)
  Password+=choice2
  choice3=random.randint(1,9)
  Password+=str(choice3)
 print(Password)
  
  