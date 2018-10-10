from notes import *

print('Starting Note App');

userInput = input('What will you like to do? ');
print('Performing '+userInput+' operation!');

if (userInput == 'add'):
    addNote();
elif (userInput == 'list'):
    listNote();
elif (userInput == 'remove'):
    removeNote();
elif (userInput == 'read'):
    readNote();
else:
    print('Invalid operation!');