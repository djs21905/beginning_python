# Workout Application


#Defines a dictionary that correlates a day of the week with a workout.
workout_day = {          "M" : 'Legs' ,
                         "T" : 'Cardio + Stretch' ,
                         "W" : 'Chest + Triceps' ,
                        "Th" : 'Back + Biceps',
                         "F" : 'Cardio + Stetch',
                         "Sa": 'OFF' ,
                         "S" : 'OFF' }

#Defines a dictionary that correlates the workout with a routine 
routine_dictionary = {
                        'Legs' : ['Test','yolo','swag'],
                        'Cardio + Stretch': [2] ,
                        'Chest + Triceps' :[3],
                        'Back + Biceps' : [4],
                        'Cardio + Stetch' : [5],
                        'OFF' : 'Rest' ,
                        'OFF' : 'Rest' }

# Has the user choose a day of the week
def userChoice():
        choice = input()
        if len(choice) <= 2 and choice in workout_day:
                return choice
                       
# Uses the day of the week to find the corresponding workout day                                        
def workoutDay(dictionary, day):
        for key in dictionary:
                if key == day:
                        n = dictionary[day]
                        return n

#Uses the workout day to find the routine 
def routine(dictionary, variable ):
        for key in dictionary:
                if key == variable:
                        n = dictionary[variable]
                        z = ' '.join(n)
                        return z


day = userChoice()
workout = workoutDay(workout_day,day)
workout_routine = routine(routine_dictionary, workout)

print(workout)
print(workout_routine)
