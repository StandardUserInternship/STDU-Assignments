import time
import json


#Converts words.txt to a json file
filename = 'words.txt'
words = {}

with open(filename) as fh:
    for line in fh:
        command, description = line.strip().split(None, 1)

        words[command] = description.strip()

out_file = open("words.json", "w")
json.dump(words, out_file, indent = 4, sort_keys = False)
out_file.close()

#Parses the json data and prints the word associated with the specified number
with open('words.json', 'r') as f:
    data = json.load(f)

print(data["12345"])

#Linear Congruential Generator for a random number between 11111 - 66666
def lcg(x, a, c, m):
    while True:
        x = (a * x + c) % m
        yield x


def random_uniform_sample(n, interval, seed=time.time()):
    a, c, m = 1103515245, 12345, 2 ** 31
    bsdrand = lcg(seed, a, c, m)

    lower, upper = interval[0], interval[1]
    sample = []

    for i in range(n):
        observation = (upper - lower) * (next(bsdrand) / (2 ** 31 - 1)) + lower
        sample.append(round(observation))

    return sample

#prints the generated list of size 6 for testing purposes
rus = random_uniform_sample(8, [11111, 66666])
print(rus)


#cody's portion [50-86]
file = open("words.txt", "r")

#defining the dictionary <key:value>
#takes each line as a key (ints) and value (string)
d = {}
for line in file:
    (key, value) = line.split()
    d[int(key)] = value

#logic for checking if the passed in value (n)
#is inside the dictionary
#appends the value associated with the key to the list
list = []
def logic(n):
    for x, y in d.items():
        #may need to change 'n' to an int
        #when hunter returns a list of strings
        if x == n:
            list.append(y)
    print(list)

#on hunter's function, he returns a list of the 
#user inputted amount of dices that will be rolled
#in his example its '8', so it will generate
#for example [55192, 12506, 25181, 63907, 31987, 40453, 49322, 39844]
#using for loop (for i in list), just retrieve the value pair
#associated with each and append each to a new list and return that
#return for corbyn's HTML page {{ result }}
def generatedPassword(sample):
    for i in sample:
        logic(i)
#error occurs because the numbers generated from
#11111-66666 dont exactly correlate to the .txt file from
#which we input the passwords from
#so my loop (cody's) doesnt recognize that the strings
#arent even in my dictionary to begin with
generatedPassword(rus)