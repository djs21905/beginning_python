#Gallows class that defines the function gallows.
#Allows the user to choose and integer ranging from 0-6
#  Each value corresponds to a different image displayed
#  0 = No body parts
#  1 = Head
#  2 = Head and Torso
#  3 = Head , Torso and Right arm
#  4 = Head , Torso , Right and Left arms
#  5 = Head , Torso , Right and left arms , right leg
#  6 = Head , Torso , Right and left arms , right and left leg 
#  COMPLETED ON 01/23/17 


# Defines the function gallows.  Requires an integer 0-6.
def gallows(number):
    top_peice = '    -------+'
    pole1 = '    |\n'
    pole2 = '    |\n'
    pole3 = '    |\n'
    base =  '=========='
    
    # Replaces the string with a new string depending on the number argument passed to the function
    if number >= 1:
        pole1 = '    |      O \n' # Head
    if number >= 2:
        pole2 = '    |      |\n'  # Torso
    if number >=3:
        pole2 = '    |     /|\n'  # Torso Right arm
    if number >=4:
        pole2 = '    |     /|\\\n' # Torso Right + Left arms
    if number >=5:
        pole3 = '    |     / \n'   # Right Leg
    if number >=6:
        pole3 = '    |     / \\\n' # Right + Left legs
    
    # Assigns each string object to the list gallowList 
    gallowList = [top_peice, pole1, pole2, pole3, base]

    # Prints each list item to the console
    for x in gallowList:
            print(x)
    
            
