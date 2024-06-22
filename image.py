from image_to_ascii import ImageToAscii

# Prompt the user for an image file path. +
# Load the image and convert it to ASCII art. +
# Display the ASCII art. +
# Implement error handling for missing or invalid files.+

# Create a repository for the project.
# Push the Python script to the repository.
# Invite the user "founderblocks-sils" to the repositor


def ask_user():
    path = input("Where to save the Ascii file: ")
    image_name = input("Please enter an image file path: ")
    try:
        image = ImageToAscii()
        image.image_path(image_name)
        image.plot()  
        image.save_to_file() 
    except:
        print("An error has occured.")    

def picture_conversion(): 
    end_program = False
    while not bool(end_program):
        choice = ''

        print(('\n') + "Select a choice: ")
        print("Option 1: Put in file")
        print("Option 2: ?")
        print("Option 3: End program")
        choice = input("Enter (1/2/3): ")

        if choice in ['1', '2', '3']:
            match choice:
                case '1':
                    ask_user()
                case '2':
                    a = 1
                case '3':
                    print("End program")
                    end_program= True
        else: 
            print(('\n') + "Invalid choice. Please enter a number between 1 and 3.")   

picture_conversion()
