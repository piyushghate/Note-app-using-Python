import json

# Fetch all the Notes stored on data.json file
def fetchNote():
    try:
        openFile = open('data.json', 'r');
        return json.load(openFile);
    except:
        return [];

# function to save the notes in data.json file
def saveNotes(parseFile):
    with open('data.json', 'w') as testfile:
        json.dump(parseFile, testfile);    

# Adding a Note to data.json file
def addNote():
    print ('Adding a Note');
    parseFile = fetchNote();

    title1 = input('Title? ');
    body1 = input('Body for the given title? ');

    data = {
            'title' : title1, 
            'body': body1
         };
         
    def duplicateFunc():
        for each in parseFile:
            if (each['title'] == data.get('title')):
                return True;
            else:
                return False;

    if (duplicateFunc()):
        print('Title already exists!!!');
        print('Note not added!!');
    else:    
        parseFile.append(data);
        saveNotes(parseFile);
        print('Note with title: '+data.get('title')+ ' added!');

# Listing all the Notes from data.json file
def listNote():
    parseFile = fetchNote();
    for each in parseFile:
        print('Title: '+ each['title']+ ' Body: '+each['body']);

# Remove a note from data.json file
def removeNote():
    print('Removing a Note');
    parseFile = fetchNote();
    titleRemove = input('What you want to delete? ');
    for each in parseFile:
        x = False;
        if(each['title'] == titleRemove):
            parseFile.remove(each);
            x = True;
            break;
    if (x == True):
        saveNotes(parseFile);
        print('Note with title: '+titleRemove+ ' removed!');
    else:
        print('Nothing found');

# Read a note from data.json file
def readNote():
    print('Reading a Note');
    parseFile = fetchNote();
    title1 = input('Title to be read? ');
    for each in parseFile:
        x = False;
        if (each['title'] == title1):
            print('Body for the title '+title1+' is '+each['body']);
            x = True;
            break;
    if(x == True):
        pass;
    else:
        print('Note with Title: '+title1+' does not exists!!');
