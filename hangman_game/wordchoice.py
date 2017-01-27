# Class for choosing a word 

class MysteryWord():

        def __init__(self, word):

                self.word = word

        # Allows you to check if a word is valid
        # For a word to be "valid" it must NOT contain any invalid characters
        # It must also be greater than 0 characters 
        def valid(self):
                word_is_valid = True
                invalid_characters = list('0123456789!@#/<>`~!.?')
                for char in invalid_characters:
                        if char in self.word or len(self.word) < 1:
                                word_is_valid = False 
                                return word_is_valid  

                return word_is_valid 

        # Returns the index Values of the spaces in a word if they exist 
        # If no spaces exist, it returns an empty list 
        # This value can then be used as an argument in the drawBoardWithSpaces method 
        def indexOfSpaces(self):
                word_as_list = list(self.word)
                index_of_spaces = []
                for index , char in enumerate(word_as_list):
                        if ' ' in char:
                                index_of_spaces.append(index)
                return index_of_spaces
                 





