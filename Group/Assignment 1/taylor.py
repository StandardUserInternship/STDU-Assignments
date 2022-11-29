import time
import datetime
import PIL
import json


#roll dice to generate random 5 digit number between 11111 and 66666

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
print(roll)

#open txt file for words to match with generated number 
file = open("words.txt")
data = file.readlines()
matchwords = []
for line in data:
    row = line.split()
    if row[0] == roll:
        matchwords.append(row[1])




#print out word that match with the generated number
for word in matchwords:
    print(word)
       
       