# Instructions on how to run my application

## Steps to install

The user should be able to open their terminal and type ./run.sh
this sh file will:

- python3 -m venv dnd-venv -create a virtual environment for the user called dnd-venv-
- source dnd-venv/bin/activate -activates the virtual enviornment-
- pip3 install -r requirements.txt -installs my dependencies and libraries-
- clear -clears terminal for a clean start-
- python3 main.py -starts the program-

## Dependencies

colored==1.4.4
iniconfig==2.0.0
packaging==23.1
pluggy==1.0.0
pytest==7.3.1

all should be installed in the ./run.sh

## System/Hardware requirements

There are no requirements outside of terminal access, the program requires minimal power and should run on all computers.

## How to use any command line arguments made for the application

after using ./run.sh you will navagate through my application in 2 ways:

1. You'll be prompted to input a number for example,

- the start menu selection will be from 1 - 4 inclusive.

- the class selection will give you options from 1 - 12 with the numbers corrosponding to the class you wish.

2. User input:

- When creating a name you'll input any name you wish, this part has no error handling as its up to the user.

- when editing, or viewing a character you'll be prompted type in the name you wish from the list printed, case is ignored here but you will have to type the name correctly or it will loop back and ask again.

- when editing class/stats you'll be prompted to type in class or strenght etc then prompted again to input your new class or stat, this is left open incase the user wants to input an entirely new class or to increase a stat higher past the starting 18pt threshhold.
