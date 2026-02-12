# Login System
#### Video Demo: (https://youtu.be/6Fd8buPcUew)
#### Description:
A simple python program that instructs users to either log in with an existing username and password, or to generate one themselves.
Generating one adds the user to a csv where they can then log into the system.
Currently, the program just prints "Hello, [user]" upon a successful login, but with more advanced systems, it would give access to the rest of the program.

My project consists of 4 files for functionality;
- project.py
- test_project.py
- requirements.txt
- information.csv

#### project.py
project.py is the main file that the program runs on. It holds all of the code for the login and creation functions, as well as two functions for generating the username and password - separated for tidiness of code - and a descision function.

The main function lays out the main menu and calls the descision function to handle the descision making from the user. It also handles an incorrect alphabetical input from the user, should they not pick numerically.

The descision function serves as a large if else statement to call the applicable function that the user chooses. It also handles incorrect selections from the user, should they choose to type a number not in the options list. This function also handles the input the user must give before the functions are called. For example, the username and password for the login function. This layout was chosen as to improve possibility of successful tests.

The login function takes the username and password and opens the information.csv. It adds all the lines to a list of dictionaries and iterates through it, checking for a match of username and password. If it matches, then the program prints "Hello," followed by the first and last name attached to the account. If it finds a match to the username but not the password, then it prints the phrase "Incorrect Password". If none of the information is correct, then it requests that the user should create an account.

The create function takes a full name that the user inputs and splits it into a first and last name. Two ways of writing the full name are accepted; "John Doe", and "Doe, John". This was chosen as it was a discussed issue during some of the lectures and it stuck in my head that it was something to watch out for. It takes the first name and sends it to the gen_user function, which will return a username with the following format "John_123", and calls the gen_pass function to create a password with the following format "abc1234". These two are then printed so the user can see what their login information is, and then saved alongside the user's full name to information.csv to be read when the user next logs in.

the generation functions both do rougly the same thing as each other, where they generate 3 or 4 random numbers and sometimes letters, and returns the final username and password to the create function.

#### test_project.py
test_project.py is the test file to check that each of the isolated functions are working as intended. Thanks to the randomised nature of most of my functions, the tests are short in nature, but still able to assert the correct responses from their intended places. All of these tests come back successful.

####This Repository is Archived and will not continue to be updated.
