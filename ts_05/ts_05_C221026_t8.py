# Parent class
class FileManager:
    #constructor
    def __init__(self, filename):
        self.filename = filename

    #writing user input to the file
    def write_in_file(self, message):
        try:
            with open (self.filename, "w") as file:
                file.write(message)
        except Exception as e:
            print(f"Error writing to the file: {e}")

    #reading the content from the file
    def read_from_file(self):
        try:
            with open(self.filename,"r") as file:
                content = file.read()
                print("\nFrom file:", content)
        except FileNotFoundError:
            print("File not found. Creating the file...")
            self.create_file()
            self.read_from_file()
        except Exception as e:
            print(f"Error writing to the file: {e}")

    #creates the file if the file doesn't exist
    def create_file(self):
        try:
            with open(self.filename, "w") as file:
                file.write("")
        except Exception as e:
            print(f"Error writing to the file: {e}")


#main program
message = input("Enter the content to write into the file: ") # taking user input

file_manager = FileManager("User_input.txt") # creating object

file_manager.write_in_file(message) # writing the user input into the file using object

file_manager.read_from_file() # reading from the file

#duttaturja