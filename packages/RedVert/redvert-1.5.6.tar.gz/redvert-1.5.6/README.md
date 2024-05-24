# @COPYRIGHT 2024 By Kyfstore

# Introduction

Hello! This is RedVert, the python package similar to anaconda where you can create environment folders, variables and other python scripts! These scripts may not be posted, stolen or copyrighted as your own.

# The Basics

To use this new python module, first type in a terminal or cmd,
```
pip install RedVert
```
After the installation process open up your coding software, in this case VS Code, and in a new .py file type in,
```
from redvert import *
```
That's how you init (initalize) it in python. Although this pip software also works in the terminal! Read the next part to learn more.

# How To Init It In Terminal

To init RedVert in the terminal, first open file explorer and go to the file location you want your RedVert files and database environments to be stored. Next at the top, click it and type cmd. It will open a cmd prompt in that location. If this doesn't work, open a normal cmd and use this code,
```
cd ('your folder path goes here')
```
Now here, type in terminal,
```
redvert
```
This will init it! I will now show you how to use it in terminal.

# How to use in terminal

When Inited, it will probably show up something like this,
```
Welcome To RedVert. What would you like to do?
Create Env, Access Env, Remove All Env, Clear Console
```
The first cmd is 'Create Env' which stands for create environment. So, type in the input, create env and it will prompt you with this text.
```
Name Environment
```
Name the environment and wala! In your folder is a new text document containing your new environment. To access it, it should be pretty straight forward. Just input,
```
Access Env
```
And put in your env name in the input. You've now acessed your new env! Now, once again, it will prompt you with some more text.
```
What Would You Like To Do
Go Back, Create RedVert, Run RedVert, Edit RedVert
```
If you put in, 'Go Back' it will return you to the title screen. Otherwise, you can create a redvert file. Just input,
```
Create RedVert
```
And Name the file. It will then prompt you if you want to open it or not, if you choose yes, it will start up notepad and open the file, otherwise it will continue. The coding tutorial will be much further below. After coding, you can run it by typing,
```
Run RedVert
```
And put in the name and it will automatically run the file for you! The last command is,
```
Edit RedVert
```
First, input it and it will prompt you with the name of the script. Please do not include the .redvert when inputing the filename. That's everything!
Now go back to the home screen. After running the file, you will be prompted the beginning text. If you want you may clear the envs file yourself, otherwise you can type,
```
Remove All Env
```
And if you are sure you want to do this, type in,
```
y
```
And all of your envs are deleted! The final RedVert cmd is,
```
Clear Console
```
After entering, the console will be cleaned up but the program will still be active. So if anyone tries to see what you did in RedVert, they are going to have a hard time trying to figure it out. To actually stop redvert use the command below on the home screen:
```
Stop RedVert
```
After running the command, it will stop redvert and you can continue from there.

# How To Use RedVert In Python

You now may be wondering, 'Uhh, how do you use this in python?' well this section tells you all about it! Well, just like before, to init in python just type,
```
from redvert import *
```
Now there are a few functions you can run. The mains ones are,
1. Initalize
2. createNewFile
3. save_to_file
4. loadfile
5. remove_content_from_file
6. append_to_file
7. interpret

These are the core basics of the RedVert python module. (NOTE: The first function is actually the function that is ran in the terminal, to really visualize whats happening not through the terminal, use the initalize function and observe what happens in the folder.)

To create a new file, you first have to import redvert, next create a variable storing the filename.
```
from redvert import *

filename = 'whateverfilenameyouwant.txt' # The extension of the file doesn't matter, in this case, I'm using .txt

```
Now use the createNewFile to create it in the base folder.
```
from redvert import *

filename = 'whateverfilenameyouwant.txt' # The extension of the file doesn't matter, in this case, I'm using .txt

createNewFile(filename)

```
Wala! The new file is created. Now we're going to learn more about the save to file and append to file functions.
To save one file of code to the file, use the save to file cmd, otherwise use append to file to append multiple lines.
To use save_to_file you put the input in the first param, and put the file name in the second.
```
from redvert import *

filename = 'whateverfilenameyouwant.txt' # The extension of the file doesn't matter, in this case, I'm using .txt

createNewFile(filename)
save_to_file('hello world', filename)
```
And After Running the .py code, you should see a new file with the name you wanted with the text you put in! Congrats!
To use append_to_file, do the samething as before, just replace it.
```
from redvert import *

filename = 'whateverfilenameyouwant.txt' # The extension of the file doesn't matter, in this case, I'm using .txt

createNewFile(filename)
append_to_file('hello world', filename)
```
And now it appends the new text to the file, remember it doesn't come with formatting.
The loadfile cmd allows you to read the file and return the output, here's an example of it working here.
```
from redvert import *

filename = 'whateverfilenameyouwant.txt' # The extension of the file doesn't matter, in this case, I'm using .txt

createNewFile(filename)
append_to_file('hello world', filename)
loaded_file = loadfile(filename)
print(str(loaded_file))
```
After running the code, you should see the text print out in the terminal!
Finally the interpret command, if you manually created a .redvert file, you can run it through python. Just use the interpret function and supply it with the file name.
```
from redvert import *

filename = 'test.redvert'
createNewFile(filename)
# Here put in the code for the redvert file, either through appending and manually doing it by hand
interpret(filename)
```

# Coding In A .RedVert File (BASICS)

This is the time where you learn how to code a .redvert file.
Below is going to be a simple hello world program, and underneath it is a little more complex program.
Here are the main funcs in a .redvert file.
1. read
2. print
3. add
4. sub
5. jump.eq.0
6. jump.gt.0
7. halt
8. push
9. pop

To use print it is pretty straight forward.
```
print "hello world"
halt
```
Remember, you must use halt at the end or else the interpret function will just completely break.
Interpreting it through the .py file, it prints hello world in the terminal! Congrats! You just coded your first ever redvert script program! 
Next up, we will be using some of the other ones so strap yourself in for a lot of coding!

# Coding In A .RedVert File (INTERMEDIATE)

First, we want to have the person input 2 values, so use the read cmd. Read inputs nothing so the user can put in any two values.
Our Current Program
```
read
read
halt
```
Next We want to subtract both of the numbers so we use the sub command.
Our Current Program
```
read
read
sub
halt
```
Next, we use the jump.eq.0 or Jump when value in stack equals 0. We need a new label, so to create it, name it and end it with a colon (:) and put the label name at the end of jump.eq.0
Our Current Program
```
read
read
sub
jump.eq.0 L1
halt

L1:
# Nothing is here
halt
```
Next, if if doesn't jump, we want it to say not equal, so after the jump.eq.0 if it didn't jump it will continue so put after the jump.eq.0, print "not equal" halt.
Our Current Program
```
read
read
sub
jump.eq.0 L1
print "not equal"
halt

L1:
# Nothing is here
halt
```
Finally, in the label, we want it to say equal, so our finished program should look something similar to this.
Our Final Program
```
read
read
sub
jump.eq.0 L1
print "not equal"
halt

L1:
print "equal"
halt
```
Congrats! You just wrote a pretty complex program. If you run it it will prompt you with two values, and it will tell you if they are equal or not. (NOTE: this is only a beginner intermediate program so errors will occur if the input is not a int or float.) We will go over pop and push later on!

# Coding Through Python Itself

If you are wondering how to code manually through python this is the section for you! First import the module and create the variable containing the filepath.
```
import redvert as rv
redvertFile = 'file.redvert'

```
Next create the file using the redvert.createNewFile function
```
import redvert as rv
redvertFile = 'file.redvert'
rv.createNewFile(redvertFile)
```
Next, you have to save the multiple lines of code. To do this, use the save_to_file function and the triple apostrophe.
```
import redvert as rv
redvertFile = 'file.redvert'
rv.createNewFile(redvertFile)
rv.save_to_file('''
print "Hello, World!"
halt
''')
```
This script will now create a new file with the file name, "file.redvert" and save a redvert command to print, "Hello, World!" Finally, you have to run it through the interpret function.
```
import redvert as rv
redvertFile = 'file.redvert'
rv.createNewFile(redvertFile)
rv.save_to_file('''
print "Hello, World!"
halt
''')
rv.interpret(redvertFile)
```
When you run this code a new redvert file will be created and it will run! In the terminal it should say Hello World! If it worked, congrats! You have successfully created a script through python!

# Other RedVert Flags

In the cmd prompt or terminal, you can type in this
```
redvert -h
```
To learn more about the flags in RedVert. One flag is the version. To see the version, just input
```
redvert --version
```
Or you can input,
```
redvert --learn-more
```
To Learn More About It. (NOTE: The learn more will only bring you back to this page.)

# Conclusion

If you read through this entire description. Well Done! You have learned a lot. This project has taken me over 3 days to make, and it is still in the beta phase. That's all for RedVert. Goodbye!