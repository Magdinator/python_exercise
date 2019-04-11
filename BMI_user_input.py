""""
IBM calculator and daily calorie needs (BMR) check (Mifflin-St Jeor method)
"""


# collecting information from user
def weight_in():
    while True:
        try:
            weight = float(input("Provide your weight in kilograms: "))
            break
        except ValueError:
            print("Incorrect input, try again")
    return weight

def height_in():
    while True:
        try:
            height = float(input("Provide your height in meters: "))
            break
        except ValueError:
            print("Incorrect input, try again")
    return height

def age_in():
    while True:
        try:
            age = float(input("Provide your age in years: "))
            break
        except ValueError:
            print("Incorrect input, try again")
    return age

def sex_in():
    while True:
        sex = input("Are you a male(M) of a female(F)?: ")
        if sex.upper() != "M" and sex.upper() != "F":
            print("Incorrect input, try again")
        else:
            break
    return sex

def bmi_count():
    weight = weight_in()
    height = height_in()
    result= weight/height**2
    return result

def bmi_score():
    result = bmi_count()
    print("Your BMI is: {}".format(result))
    if (result < 18.5):
        print("You are underweight.")
    elif (18.5 <= result < 24):
        print("Your weight is correct")
    elif (24 <= result < 26.5):
        print("You are slightly overweight")
    else:
        print("Obesity!")
        if (30 >= result > 35):
            print("You have first degree obesity")
        elif (35 >= result > 40):
            print("You have second degree obesity")
        else:
            print("You have third degree obesity")


def bmr():
    #daily calorie needs check
    sex = sex_in()
    weight = weight_in()
    height = height_in()
    age = age_in()
    if sex == "M":
        result = (9.99 * weight) + (6.25 * height * 100) - (4.92 * age) + 5
        print("Your daily calorie need is {}".format(result))

    else:
        result = (9.99 * weight) + (6.25 * height * 100) - (4.92 * age) - 161
        print("Your daily calorie need is {}".format(result))
    return result




