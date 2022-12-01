import time

#roll dice with time function 
def roll_dice():
 
    curr = str(time.time()).split('.') #getting current time and splitting it into two strings after the decimal place

    curr = curr[1] #taking the second string (numbers after the decimal point)

    dice = [] #empty list to store the dice roll 

    while True:
        #for loop to filter through each number in the string 
        for cu in curr: 
            try:
                num = int(cu) #turn each element into integer data type 

                #get only the number between 1 and 6 and collect only 5 numbers for the roll 
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
def get_word(roll):

    #open text file 
    file = open("words.txt")
    data = file.readlines()
    matchwords = [] #empty list for the matchwords 
    for line in data:
        row = line.split()
        if row[0] == roll:
            matchwords.append(row[1])

    return matchwords #return word that matches with roll 


#calulate number of possible passwords based on number of rolls 
import math
def possible_passwords(num_rolls):
    
    #initialize the number of items to chose from 
    n = 7776

    #initialize possiblilies to choose from 
    k = num_rolls
    
    passwords = math.comb(n,k)

    #return total number of combinations formatted 
    return format(passwords, ',d')

#main function
def main():
    t = 5
    #return


user = possible_passwords(2)
print(user)
