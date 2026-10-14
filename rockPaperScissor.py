import random
print("welcome to the rock paper scissor game:")
ch =input("wanna play enter y ").strip().lower()
while(ch=='y'):
    computer = random.choice(["rock","paper","scissor"])
    print(computer)
    choice =input("enter you choice between rock,paper,scissor :  ").lower().strip()
    if choice not in ["rock","paper","scissor"]:
        print("invalid choice! please choose between rock paper or scissor")
        break
    if choice==computer:
        print("draw")
    elif choice=="paper" and computer=="rock" or choice == "scissor"and computer=="paper" or choice =="rock" and computer=="scissor":
        print("yay!!!! you won ")
    else:
        print("you lost ")
    ch =input("wanna play enter y ").strip().lower()