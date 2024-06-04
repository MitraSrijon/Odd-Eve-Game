import time
import random

print("_________________________________________")
print("Following are the rules of the game")
print("1. First we will have a toss. You can call H for heads and T for tails")
print("2. If you win the toss you can decide whether you want to bat or bowl")
print("3. If the number you enter does not match with computer all the entered numbers will get added to you score")
print("4. If you are bowling , then to take a wicket , there should be a match between your entered number and computer number.")
print("_________________________________________")

print()
time.sleep(8)

print("We are all set to start. ")
time.sleep(1)

print("_________________________________________")
print(f"Let the game begin")
print("-----------------------------------------")

time.sleep(2)

#Required Varibles
toss_pos = ("H", "T")
comp_opt = ("Bat","Bowl")
user_score = 0
comp_score = 0
comp = (1,2,3,4,5,6)

#If user wins toss and bat first
running_b1 = True
running_bo1 = True

#If user wins the toss and bowl first
running_b2 = True
running_bo2 = True

#If computer wins and bat fist
running_c1 = True
running_co1 = True

#If computer wins and bowl fist
running_c2 = True
running_co2 = True

#Toss
toss_pos = ("H", "T")
print("Its time for the toss..........")

time.sleep(1)

toss = input("Whats your call (H/T)?").upper()

#result varible will store the random characeter from toss_pos tupple which will help to identify who wins the toss
result = random.choice(toss_pos)
print(result)

time.sleep(1)

#If the result matches with the input of user then user wins the match otherwise computer wins
if(toss == result):
    print("Congratulations! You won the toss")
    time.sleep(1)

    choose = input("What would you like to do(Bat/Bowl)?").lower()
    time.sleep(1)

    print(f"Lets Begin. You are {choose}ing first")
    time.sleep(1)

    print()
    print("-----------------------------------------")
#In this case we have won the toss and elected to bat first
    if choose == "bat":
        while running_b1:
            user_input = int(input("Enter your number(1,2,3,4,5,6) : "))
            comp_select = random.choice(comp)

            print(f"Computer's number {comp_select}")
            if user_input != comp_select:
                user_score += user_input
            else:
                print("Opps your are out!")
                running_b1 = False

        print()
        print(f"You have scored {user_score} runs")
        time.sleep(1)
        print(f"Target for computer is {user_score + 1}")

        print()
        print("-----------------------------------------")

        time.sleep(1)
        print("Its time for computer to bat. Its your bowling now")
        while running_bo1:
            user_input = int(input("Enter your number(1,2,3,4,5,6) : "))
            comp_select = random.choice(comp)

            print(f"Computer's number {comp_select}")
            if user_input != comp_select:
                comp_score += comp_select
                if comp_score > user_score:
                    print(f"Score of computer is {comp_score}")
                    print("Computer Wins!")
                    break
            else:
                print("You took the wicket of computer.")
                print(f"Score of computer is {comp_score}")
                print("You are the winner!")
                running_bo1 = False

        print()
        print("-----------------------------------------")


#In this case we have won the toss and elected to bowl first
    else:
        while running_bo2:
            user_input = int(input("Enter your number(1,2,3,4,5,6) : "))
            comp_select = random.choice(comp)

            print(f"Computer's number {comp_select}")
            if user_input != comp_select:
                comp_score += comp_select

            else:
                print("You took the wicket of computer.")
                running_bo2 = False

        print()
        print(f"Computer has scored {comp_score} runs")
        time.sleep(1)
        print(f"Target for you is {comp_score + 1}")
        time.sleep(1)
        print()

        print("-----------------------------------------")

        print("Its time for computer to bowl. Its your bating now")
        while running_b2:
            user_input = int(input("Enter your number(1,2,3,4,5,6) : "))
            comp_select = random.choice(comp)

            print(f"Computer's number {comp_select}")
            if user_input != comp_select:
                user_score += user_input
                if user_score > comp_score:
                    print(f"Your score is {user_score}")
                    print("You are the winner!")
                    break
            else:
                print("Opps you are out!")
                print(f"Your score is {user_score}")
                print("Computer Wins!")
                running_b2 = False

        print()
        print("-----------------------------------------")

#Computer wins the toss
else:
    print("Opps computer wins the toss")
    computer = random.choice(comp_opt)
    print(computer)

    time.sleep(1)

    print()
    print(f"Computer decides to {computer} first")

    #Computer elects to bat first
    if computer == "Bat":
        print("You are bowling first")
        while running_c1:
            user_input = int(input("Enter your number(1,2,3,4,5,6) : "))
            comp_select = random.choice(comp)

            print(f"Computer's number {comp_select}")
            if user_input != comp_select:
                comp_score += comp_select

            else:
                print("You took the wicket of computer.")
                running_c1 = False

        print()
        print(f"Computer has scored {comp_score} runs")
        time.sleep(1)
        print(f"Target for you is {comp_score + 1}")
        time.sleep(1)
        print()
        print("-----------------------------------------")
        print("Its time for computer to bowl. Its your bating now")
        while running_co1:
            user_input = int(input("Enter your number(1,2,3,4,5,6) : "))
            comp_select = random.choice(comp)

            print(f"Computer's number {comp_select}")
            if user_input != comp_select:
                user_score += user_input
                if user_score > comp_score:
                    print(f"Your score is {user_score}")
                    print("You are the winner!")
                    break
            else:
                print("Opps you are out!")
                print(f"Your score is {user_score}")
                print("Computer Wins!")
                running_co1 = False

        print()
        print("-----------------------------------------")

    else:
        print("You are batting first")
        while running_c2:
            user_input = int(input("Enter your number(1,2,3,4,5,6) : "))
            comp_select = random.choice(comp)

            print(f"Computer's number {comp_select}")
            if user_input != comp_select:
                user_score += user_input
            else:
                print("Opps your are out!")
                running_c2= False

        print()
        print(f"You have scored {user_score} runs")
        time.sleep(1)
        print(f"Target for computer is {user_score + 1}")

        time.sleep(1)
        print()
        print("-----------------------------------------")
        print("Its time for computer to bat. Its your bowling now")
        while running_co2:
            user_input = int(input("Enter your number(1,2,3,4,5,6) : "))
            comp_select = random.choice(comp)

            print(f"Computer's number {comp_select}")
            if user_input != comp_select:
                comp_score += comp_select
                if comp_score > user_score:
                    print(f"Score of computer is {comp_score}")
                    print("Computer Wins!")
                    break
            else:
                print("You took the wicket of computer.")
                print(f"Score of computer is {comp_score}")
                print("You are the winner!")
                running_co2 = False

        print()
        print("-----------------------------------------")
