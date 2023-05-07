# Documentation for T1A3 terminal application

## R3 - Sources

[f-strings](http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf) 

[random number guide](https://www.programiz.com/python-programming/examples/random-number#:~:text=To%20generate%20random%20number%20in,is%20defined%20in%20random%20module.) 

[removing .csv from file when printing for user](https://stackoverflow.com/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python) 

[using glob import](https://docs.python.org/3/library/glob.html)

[finding files in directory](https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python) 

[combining 2 pieces information into a dictionary](https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/)

## R4 - Link to source control repository.



## R5 - Code styling and styling conventions

For my Terminal application i used PEP 8
I used:

- 4 spaces for indentation thoughout my code as seen below example
[4 space example](/docs/Screenshot%20at%20May%2007%2013-38-06.png)
- maximum 79 chartacters in the majority of my code, all my code should be as viewable as possible in a single window with very few exceptions if any.
- Imports on seperate lines in all places throughout my code, see below example
[imports](/docs/imports.png)
- String quotes aren't specified in PEP 8 as to the preferred methond but it does recommend picking 1 and sticking to it, in my application I have predominately used double quotes where possible with exception to areas where double has already been used for a string.
- Whitespace in expressions and statements spairingly if at all sticking the to the convention of not over using whitespace where it does not aid in code readability.
- Comments, I have stuck to block comment convention except for in places where the code was quite long and I wanted to note a specific spot in the code and felt inline made more sense and was cleaner.
- I have kept to the function and variable naming convention using lowercase with words seperated like such "char_choice".

## R6 - Features

I have created 3 distinct features for my terminal applciation that will be acccesed through a start menu as such

1. Create new character -
this features involves letting the user create a new character by first asking the using to input a name, next picking from a list of classes, then finally rolling dice to generate the stats for said character, finally it will input all these details into a csv file (which is named the same as the character name input to make it easy for the user to find in the next few features) and print for the user to view.
The create function is extensive with multiple uses of local scope variables and for loops.

2. Edit character -
this features allows you to access a previously created character, prompting the user to pick from a list of characters they have created by printing any csv names to the terminal. This is the largest function i created as it had the most room for user error, I created error handling in all aspects from there not being any previously created characters in which case it will print none and inform the user they haven't made any yet using while and for loops and multiple cases of local variables. The user will be able to type in the name of the file from the list they want to edit, i made this case insensitive to take out user error in that part. The user is asked what part they would like to edit then will be asked to input the new class/stats they wish their character to have. The user will be prompt on whether they want to change anymore and will either loop back through the options inpout prompt again or finish editing and return to the main start up menu.

3. View character -
this feature allows the user to access any already made characters and have the app print out whichever character they wish, this contains the same error handling for no available characters and error handling for wrong input of character they'd wish to change by prompting the user to again input the correct character.

4. Exit -
once I started this project I realised quickly that I needed to add an exit option to my list.

## R7 -

I used a mix of hand written notes and commeting at the bottom of my code to keep track of where I was at in my project, I realised after a few days that this wasn't sufficient and moved my project management plan to an online source for a cleaner more professional approach.
see link to my project management plan
-- add in monday.com link --

## R8 -

see link to my help document below.
[Help](./src/help.md)