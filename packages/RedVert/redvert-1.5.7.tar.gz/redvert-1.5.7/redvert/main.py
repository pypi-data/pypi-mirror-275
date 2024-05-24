import ast
import os
import argparse
import webbrowser
import subprocess as sp
import glob as gb
from time import sleep as delay

env_file = 'envs.txt'
env_name = {}
scriptcontainerfile = {}
scriptFiles = []  # New list to store the names of created .redvert files

def openRedVert(filename):
    os.system(f'start notepad {filename}')

def interpretRedVert(program_filepath):
    program_lines = []
    with open(program_filepath, "r") as program_file:
        program_lines = [line.strip() for line in program_file.readlines()]
    
    program = []
    token_counter = 0
    label_tracker = {}
    for line in program_lines:
        parts = line.split(" ")
        opcode = parts[0]
        if opcode == "":
            continue
        if opcode.endswith(":"):
            label_tracker[opcode[:-1]] = token_counter
            continue
        program.append(opcode)
        token_counter += 1
        if opcode == "push":
            number = int(parts[1])
            program.append(number)
            token_counter += 1
        elif opcode == "print":
            string_literal = ' '.join(parts[1:])[1:-1]
            program.append(string_literal)
            token_counter += 1
        elif opcode == "jump.eq.0":
            label = parts[1]
            program.append(label)
            token_counter += 1
        elif opcode == "jump.gt.0":
            label = parts[1]
            program.append(label)
            token_counter += 1
    class Stack:
        def __init__(self, size):
            self.buf = [0 for _ in range(size)]
            self.sp = -1
        def push(self, number):
            self.sp += 1
            self.buf[self.sp] = number
        def pop(self):
            number = self.buf[self.sp]
            self.sp -= 1
            return number
        def top(self):
            return self.buf[self.sp]
    
    pc = 0    
    stack = Stack(256)
    while program[pc] != "halt":
        opcode = program[pc]
        pc += 1

        if opcode == "push":
            number = program[pc]
            pc += 1

            stack.push(number)
        elif opcode == "pop":
            stack.pop()
        elif opcode == "add":
            a = stack.pop()
            b = stack.pop()
            stack.push(a+b)
        elif opcode == "sub":
            a = stack.pop()
            b = stack.pop()
            stack.push(a-b)
        elif opcode == "print":
            string_literal = program[pc]
            pc += 1
            print(string_literal)
        elif opcode == "read":
            number = int(input())
            stack.push(number)
        elif opcode == 'jump.eq.0':
            number = stack.pop()
            if number == 0:
                pc = label_tracker[program[pc]]
            else:
                pc += 1
        elif opcode == 'jump.gt.0':
            number = stack.pop()
            if number > 0:
                pc = label_tracker[program[pc]]
            else:
                pc += 1

def save_to_file(fileinput, filename):
    with open(filename, 'w') as file:
        file.write(fileinput)

def append_to_file(fileinput, filename):
    with open(filename, "a") as file:
        file.write(fileinput)

def loadfile(filename):
    with open(filename, 'r') as file:
        read = file.read()
    return read

def removeEnvironments(filename):
    with open(filename, 'w'):
        pass

def deleteFile(filename):
    if os.path.isfile(filename):
        os.remove(filename)

def createNewFile(filename):
    removeEnvironments(filename)

def remove_content_from_file(filename):
    removeEnvironments(filename)

def Initalize():
    i = 0
    isRunning = True
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='RedVert Version 1.5.7')
    parser.add_argument('--learn-more', action='store_true', help='Learn More At pypi.org/project/RedVert')
    args = parser.parse_args()
    if args.learn_more:
        webbrowser.open('pypi.org/project/RedVert', new=2)
        isRunning = False
    while isRunning:
        print("Welcome To RedVert. What would you like to do?")
        print("Create Env, Access Env, Remove All Env, Clear Console, Stop RedVert")
        user_input = input('>>> ')
        if user_input == "Stop RedVert":
            print("Successfully Stopped RedVert\n")
            isRunning = False
            break
        elif user_input == 'Create Env':
            print("Name Environment")
            env_input = input('>>> ')
            if env_input.strip():  # Check if the input is not empty or whitespace only
                env_name[f'env{i}'] = env_input.strip()  # Store the input without leading/trailing whitespaces
                save_to_file(str(env_name), env_file)
                print("Successfully Created Environment\n")
                i += 1
            else:
                print("You cannot create an environment with no name\n")
        elif user_input == 'Remove All Env':
            print("Are you sure [y or n]")
            remove_input = input('>>> ')
            if remove_input == 'y':
                print("Clearing All Data")
                print("1% Completed")
                delay(0.7)
                print("7% Completed")
                delay(0.7)
                print("15% Completed")
                delay(0.4)
                print("25% Completed")
                delay(0.9)
                print("49% Completed")
                delay(0.7)
                print("69% Completed")
                delay(0.7)
                print("88% Completed")
                delay(1)
                print("100% Completed")
                delay(1.2)
                values = {}
                print("Successfully removed all environments!\n")
                removeEnvironments(env_file)
                delay(1)
                deleteFile(env_file)
                # Delete .txt and .redvert files associated with each script file
                for scriptFile in scriptFiles:
                    deleteFile(f'{scriptFile}.txt')
                    deleteFile(f'{scriptFile}.redvert')
            elif remove_input == 'n':
                print("Canceled Remove\n")
                continue
            else:
                print("Expected Y or N. Invalid")
                continue
        elif user_input == "Clear Console":
            print("Clearing Console")
            delay(1.2)
            if os.name == "nt":
                sp.call('cls', shell=True)
            else:
                sp.call('clear', shell=True)
        elif user_input == "Access Env":
            print("Access Which Env")
            env_input = input('>>> ')
            try:
                with open('envs.txt', 'r') as f:
                    read_file = f.read()
                if env_input in read_file:
                    print("Successfully Found Env\n")
                    current_env = env_input
                    print("What Would You Like To Do")
                    print("Go Back, Create RedVert, Run RedVert, Edit RedVert")
                    user_input2 = input('>>> ')
                    if user_input2 == 'Go Back':
                        continue
                    elif user_input2 == "Create RedVert":
                        print("Creating a .redvert File")
                        print("What Do you want the file to be called?")
                        name_input = input('>>> ')
                        scriptFiles.append(name_input)  # Add the script file name to the list
                        script_parent_container = f'{name_input}.txt'
                        py_file = f'{name_input}.redvert'
                        print(f"Creating {py_file}.")
                        removeEnvironments(py_file)
                        removeEnvironments(script_parent_container)
                        scriptcontainerfile['parent'] = current_env
                        save_to_file(str(scriptcontainerfile), script_parent_container)
                        print("Completed Creating File")
                        print("Do you want to open this file it NotePad? [y or n]")
                        openInput = input(">>> ")
                        if openInput == "y":
                            openRedVert(f"{name_input}.redvert")
                        elif openInput == "n":
                            print("")
                        else:
                            print("Unknown Command\n")
                    elif user_input2 == "Run RedVert":
                        print("Please Name The .redvert File You Want To Run.")
                        redvertname = input('>>> ')
                        try:
                            values = ast.literal_eval(loadfile(f'{redvertname}.txt'))
                            if values['parent'] == current_env:
                                print("Successfully Ran RedVert File")
                                interpretRedVert(f'{redvertname}.redvert')
                        except:
                            print("RedVert File Is Non Existent\n")
                    elif user_input2 == "Edit RedVert":
                        print("What is the name of the .redvert file you want to access?")
                        name_input2 = input(">>> ")
                        try:
                            values = ast.literal_eval(loadfile(f'{name_input2}.txt'))
                            if values['parent'] == current_env:
                                openRedVert(f"{name_input2}.redvert")
                                print("Opened File\n")
                        except:
                            print("RedVert File Is Non Existent\n")
                    else:
                        print("Unknown Command Please Try Again\n")
                        continue
                else:
                    print("Unknown Environment\n")
            except:
                print("Unable To Open Environments File\n")
        else:
            print("Unknown RedVert Command Try Again.\n")