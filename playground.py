# f = open('try.txt', 'w');

# for i in range(1,11):
#     f.write('This is line %d\n' %i);

# print ('task completed!!');

import json

# title = None;
# body = None;

# data = ('piyush', 'ghate');

# x = str(data);

# y = json.dumps(x);
# print(y);

# print(str(y));

# with open('test.json') as jsonfile1:
#     parseFile = json.loads(jsonfile1);

# jsonfile1 = open('test.json');

# parseFile = json.load(jsonfile1);

# print(parseFile);
        # for lines in jsonfile1:
        #     print(lines);
        #     print('\n');

# try:
#     openFile = open('test.json', 'r');
#     print(openFile);
#     parseFile = json.load(openFile);
#     print(parseFile);
# except:
#     parseFile = [];

# title1 = input('Title? ');
# body1 = input('Body for the given title? ');

# data = {
#             'title' : title1, 
#             'body': body1
#          };

# parseFile.append(data);

# with open('test.json', 'w') as testfile:
#     json.dump(parseFile, testfile);

data = {
            'title' : 'pulkit', 
            'body' : 'body1',
         };

# print(data.get('title'));

###################################filter#################################
try:
    openFile = open('test.json', 'r');
    print(openFile);
    parseFile = json.load(openFile);
    print(parseFile);
except:
    parseFile = [];

list1 = {'b':2,2:'a',3:4,'c':5};

# for each in parseFile:                            #### To LIST
#     print('Title available are: '+ each['title']+ ' with body as: '+each['body']);

for each in parseFile:
    if (each['title'] == data.get('title')):
        return True;
    else:
        return False;