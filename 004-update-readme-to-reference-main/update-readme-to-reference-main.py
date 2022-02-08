from operator import truediv
import os
import os.path
from tkinter import N

script_path = os.path.dirname(__file__)
default_directory = os.path.split(script_path)[0] + "/"
default_file_name = "README.md"
directory = default_directory
file_name = default_file_name
full_path = directory + file_name

def perform_quit():
    print("Quitting update-readme-to-references-main.py. Cheers!")
    quit()

def reset_path_parameters():
    global directory
    global file_name
    directory = default_directory
    file_name = default_file_name

def present_invalid_input_paremeter(invalid_input):
    exit_on_quit(invalid_input)
    invalid_input_message = "Invalid input ({}). Let's try this again shall we? (Type Q/q/Quit to exit program)"
    print(invalid_input_message.format(invalid_input))    

def exit_on_quit(input):
    if input == "q" or input == "quit":
        perform_quit()

def get_custom_directory_path():
    global directory
    finished = False

    while finished == False:
        is_custom_directory_path_required = input("Do you need a custom directory path? (y/n) ").lower()
        
        if is_custom_directory_path_required == "y" or is_custom_directory_path_required == "yes":
            directory = input("Provide fully qualified directory path: ")
            finished = True
        elif is_custom_directory_path_required == "n" or is_custom_directory_path_required == "no":
            finished = True
        else:
            present_invalid_input_paremeter(is_custom_directory_path_required)
    
    message = "Selected directory is: {}"
    print(message.format(directory))

def get_custom_file_name():
    global file_name
    finished = False

    while finished == False:
        is_custom_file_name_required = input("Do you need a custom file name? (y/n) ").lower()
        
        if is_custom_file_name_required == "y" or is_custom_file_name_required == "yes":
            file_name = input("Provide the name of the file with extension: ")
            finished = True
        elif is_custom_file_name_required == "n" or is_custom_file_name_required == "no":
            finished = True
        else:
            present_invalid_input_paremeter(is_custom_file_name_required)
        
    message = "File name is: {}"
    print(message.format(file_name))

def update_file(path):
    full_path_message = "Full path: {}"
    print(full_path_message.format(path))

    file = open(path, "r")
    file_content = file.read()

    file_content = file_content.replace('/develop/', '/main/')

    file.close()
    file = open(full_path, "wt")
    file.write(file_content)
    file.close()

def get_file_path():
    global full_path
    global directory
    global file_name
    get_custom_directory_path()
    get_custom_file_name()
    full_path = directory + file_name

def is_full_path_valid():
    finished = False
    is_path_valid = False

    while finished == False: 
        if os.path.exists(full_path) == False:
            full_path_does_not_exist_message = "Provided path ({}) does not exist. Would you lile to restart the progam? (y/n) "
            full_path_does_not_exist_message = full_path_does_not_exist_message.format(full_path).lower()
            should_restart_program = input(full_path_does_not_exist_message)

            if should_restart_program == "y" or should_restart_program == "yes":
                reset_path_parameters()
                finished = True
            elif should_restart_program == "n" or should_restart_program == "no":
                perform_quit()
            else:
                present_invalid_input_paremeter(should_restart_program)
        else:
            is_path_valid = True
            finished = True
    return is_path_valid

def request_file_path():
    global directory
    global file_name
    finished = False
    while finished == False:
        get_file_path()
        finished = is_full_path_valid()
        
reset_path_parameters()
request_file_path()
update_file(full_path)
print("Thanks for using this script! Check you repo updates. Au revoir!")