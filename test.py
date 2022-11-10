#exercise 1
print("Hello World!")
print("I am learning Python!")
print("Here is my first program.\n")

patients_name = input("What is your name? ")
print("Hello, " + patients_name)

birth_year = input("What year were you born? ")
patients_age = 2022 - int(birth_year)
print(patients_age)

patient_status = str(input("Are you a new patient? "))
if patient_status == 'Yes':
    print("Welcome! Please fill out the new patient form " + patients_name + "!")
elif patient_status == 'No':
    print("Welcome back " + patients_name + "!")
print("\n")

#exercise 2
num1 = int(input("First: "))
num2 = int(input("Second: "))
sum = num1 + num2
print("Sum: " + str(sum))
print("\n")

#exercise 3
weight = float(input("Weight: "))
letter = input("(K)g or (L)bs: ")
if letter.upper() == "K":
    conversion_1 = weight / 0.45
    print("Weight in Lbs " + str(conversion_1))
else:
    conversion_2 = weight * 0.45
    print("Weight in Kg " + str(conversion_2))
print("\n")

#exercise 4
i = 1
while i <= 69:
    print(i * "*")
    i += 1
print("\n")