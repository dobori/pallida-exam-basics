import sys

# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them



class FavAnimal(object):
    
    index = ""
    def __init__(self):
        if len(sys.argv) == 1:
            print("Usage: favoureite_animals [animal] [animal]")
        if len(sys.argv) > 1:

            self.index = str(sys.argv[2])
            return self.add_todo(self.index)

    def add_animal(self, index):
        animal_input = self.index
        self.textfile = open("favourites.txt", "a")
        self.textfile.write("0 " + animal_input + "\n")
        self.textfile.close()
