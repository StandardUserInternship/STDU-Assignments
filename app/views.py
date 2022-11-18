import json, random

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
    nameFile = open("words.txt", "r")
    words = nameFile.readlines()
    return (random.choice(words))

