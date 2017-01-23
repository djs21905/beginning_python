#Gallows class that defines the function gallows.
#Allows the user to choose and integer ranging from 0-5
#Each value corresponds to a different image displayed


def gallows(number):
    top_peice = '    -------+'
    pole1 = '    |\n'
    pole2 = '    |\n'
    pole3 = '    |\n'
    base =  '=========='
  
    if number >= 1:
        pole1 = '    |      O \n'
    if number >= 2:
        pole2 = '    |      |\n'
    if number >=3:
        pole2 = '    |     /|\n'
    if number >=4:
        pole2 = '    |     /|\\\n'
    if number >=5:
        pole3 = '    |     / \n'
    if number >=6:
        pole3 = '    |     / \\\n'
        
    gallowList = [top_peice, pole1, pole2, pole3, base]

   
    for x in gallowList:
            print(x)
       

#Tests all of the different possible drawings
""""for x in range(7):
    gallows(x)"""
            
