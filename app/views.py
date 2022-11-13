import json

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









#@app.route("/dice")
#def diceRoll():
    #return "Create a script that rolls a 6 sided dice 100 times, for each dice roll, save the results. After all 100 rolls are completed, use that data to create a single line graph utilizing pyplot."

#@app.route("/fizzbuzz", methods=['POST', 'GET'])
#def lab1():
    #listOfResults = []

    #for i in range(100):
       # if i % 3 == 0 and i % 5 == 0:
            #listOfResults.append('FizzBuzz')
       # elif i % 3 == 0:
            #listOfResults.append('Fizz')
        #elif i % 5 == 0:
            #listOfResults.append('Buzz')
       # else:
            #listOfResults(i)
    #return jsonify({'result': listOfResults})