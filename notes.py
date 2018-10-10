import json

def fetchNote():
    try:
        openFile = open('data.json', 'r');
        return json.load(openFile);
    except:
        return [];

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
        with open('data.json', 'w') as testfile:
            json.dump(parseFile, testfile);
        print('Note with title: '+data.get('title')+ ' added!');

def listNote():
    parseFile = fetchNote();
    for each in parseFile:
        print('Title: '+ each['title']+ ' Body: '+each['body']);

def removeNote():
    print('Removing a Note');
    

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
