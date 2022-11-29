import time
import datetime
import json


#roll dice with time function 
def roll_dice():
    #we need to make this more random 
    curr = str(time.time())

    dice = []

    while True:
        for cu in curr:
            try:
                num = int(cu)
                if num > 0  and num < 7:
                    dice.append(cu)
                    if len(dice) == 5:
                        break
            except:
                pass
        if len(dice) == 5:
            break

    roll = ''.join(dice)

    return roll #returns roll 


#generate words from dice roll (pass in roll variable)
def get_words(roll):

    file = open("words.txt")
    data = file.readlines()
    matchwords = []
    for line in data:
        row = line.split()
        if row[0] == roll:
            matchwords.append(row[1])

    return matchwords


def pass_phrase():
    
    



#main function
def main():
    
    #return

user = roll_dice()
print(user)