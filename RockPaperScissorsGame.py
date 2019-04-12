import random

print("_________________________________________\nWelcome to Rock, Paper and Scissors game\n_________________________________________\n for Rock o\t\t Press 1\n for Paper |_|\t\t Press 2\n for Scissors >8\t Press 3 \n To exit game\t\t Press 0\n_________________________________________\n")

name = input("Write your name:\t")

r = 'o\tRock\t\t'
p = '|_|\tPaper\t\t'
s = '>8\tScissors\t'

game = [r,p,s]

points = 0
PCpoints = 0

a = 0

while a < 5:
    print(name +" your turn, pick a number")
    x = int(input())
    if x == 0 : break
    if x == 1 :
        points += 1
        PCpoints += 1
        rand = random.choice(game)
        if rand == r:
            points -= 1
            PCpoints -= 1
        if rand == p:
            points -= 1
            a += 1
        if rand == s:
            PCpoints -= 1
            a += 1           

        print("o\tRock\t\t"+name+"\t"+str(points))
        print(rand+"PC"+"\t"+str(PCpoints))   
        

    if x == 2 :
        points += 1
        PCpoints += 1
        rand = random.choice(game)
        if rand == r:
            PCpoints -= 1
            a += 1
        if rand == p:
            points -= 1
            PCpoints -= 1
        if rand == s:
            points -= 1
            a += 1

        print("|_|\tPaper\t\t"+name+"\t"+str(points))
        print(rand+"PC"+"\t"+str(PCpoints))  
        

    if x == 3 :
        points += 1
        PCpoints += 1
        rand = random.choice(game)
        if rand == r:
            points -= 1
            a += 1
        if rand == p:
            PCpoints -= 1
            a += 1
        if rand == s:
            PCpoints -= 1
            points -= 1

        print(">8\tScissors\t"+name+"\t"+str(points))
        print(rand+"PC"+"\t"+str(PCpoints))  

print("\n"+name+" points: "+str(points)+"\tPC points: "+str(PCpoints)+"\n")
if points > PCpoints:
    print(name+" You Won, Congratulation")
    print("*$*$*$*$*$*$*$*$*$*$**$*$*$*$*$*")
else:
    print("You Lose, PC won")






    