import json, time

from flask import Flask, jsonify, render_template, request

from app import app


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fizzbuzz")
def fizzBuzz():
    return render_template("fizzbuzz.html")

@app.route("/swapcase")
def swapCase():
    return render_template("swapcase.html")

@app.route("/swapcasedata", methods=["GET", "POST"]) 
def swapCaseData():
    if request.method == "POST":
        data = request.get_json()["data"]
        data = str(data).swapcase()
        print(data)
        return jsonify({"upper": data})
    else:
        myData = 5
        return jsonify({"data": myData})
    
@app.route("/factorize")
def factor():
    return render_template("factorize.html")

@app.route("/factorizedata", methods=["GET", "POST"])
def factorizeData():
    if request.method == "POST":
        data = request.get_json()["data"]
        data = int(data)
        def factorial(n):
            fact = 1
            for i in range(1, n+1):
                fact *= i
            return fact
        print(data)
        return jsonify({"factorized": factorial(data)})
    else:
        myData = 5
        return jsonify({"data": myData})

@app.route("/diceware")
def diceware():
    return render_template("diceware.html")

@app.route("/dicewaredata", methods=["GET", "POST"])
def dicwareData():
    #Linear Congruential Generator for a random number between 11111 - 66666
    def lcg(x, a, c, m):
        while True:
            x = (a * x + c) % m
            yield x


    def random_uniform_sample(n, interval, seed=time.time()):
        a, c, m = 1103515245, 12345, 2 ** 31
        bsdrand = lcg(seed, a, c, m)
        r = 6

        lower, upper = interval[0], interval[1]
        sample = []
        outList = []
        for _ in range(r):
            for i in range(n):
                observation = (upper - lower) * (next(bsdrand) / (2 ** 31 - 1)) + lower
                sample.append(round(observation))
                num = ''.join(str(e) for e in sample)
            outList.append(num)
            sample.clear()
        return outList

#prints the generated list of size 6 for testing purposes
    rus = random_uniform_sample(5, [1, 6])
    print((rus))
    
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

    for i in range(0, len(rus)):
        rus[i] = int(rus[i])
    print(rus)

    newList = []
    def logic(n):
        for x, y in d.items():
            if x == n:
                newList.append(y)
        print(newList)

#return for HTML page {{ result }}
    def generatedPassword(sample):
        for i in sample:
            logic(i)

    generatedPassword(rus)
    return newList





#cant use random function    
#nameFile = open("words.txt", "r")
#words = nameFile.readlines()
#return (random.choice(words))

