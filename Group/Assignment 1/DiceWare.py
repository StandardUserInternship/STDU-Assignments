import random
#import pandas as pd 

#get number of dice rolls
def num_rolls(how_many_rolls):
    #get number of rolls from user 
    if how_many_rolls >= 2 and how_many_rolls <= 8:
        print('You selected ', how_many_rolls, ' rolls!')
    else:
        print('Error: Enter a number 2 - 8')




#roll dice
def roll_dice():
    r = [random.randint(1,6) for x in range(5)] #generate random dice roll from 1 to 6

    string_r = [str(x) for x in r] #makes each element in the list 

    roll = ''.join(string_r) #joins list as one numeric string 

    return roll #returns roll as the numeric string 

#generate words from dice roll 
def get_words():
    #word_df = pd.read_csv('words.txt')
    #return word_df
    t = 6
    
    



    #return words,passphrase, and possible passwords

#main function
def main():
    my = 5
    #return

user = roll_dice()
print(user)