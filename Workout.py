import pickle #converts python code to binary code 

#This is a test
#This is also a test

try:
    day = []
    bpart = []
    with open('workoutinfo.txt') as workout_document:
        for each_line in workout_document:
            (day_,body_part) = each_line.split(':')
            day.append(day_)
            bpart.append(body_part)                   
except IOError as error_:
    print('This is the error:', error_ )
    pass

while True:
    day_of_week = input("Please enter the day of the week ")
    if day_of_week in day:
            print ("Today is", len(bpart))
    else:
        print("That isnt a day of the week!")
