import json
from difflib import get_close_matches

# open and read json file
myfile = open('data.json')
data = json.load(myfile)
myfile.close()
# input word
def inputword():
    myword = input('Please enter the word: ')
    return print(translate(myword))
#  check if input match key for min 80%
def matchword(myword):
    match = get_close_matches(myword, data.keys(), n=1, cutoff = 0.8)
    if match !=[]:
        return match[0]
    else:
        return False
# output string
def output(myword, data):
    str = 'The defenition of "{}": \n'.format(myword)
    for item in data:
        str = str + item +'\n'
    return str
# return right answer
def translate(myword):
    if myword in data:
        return output(myword, data[myword])
    elif  myword.lower() in data:
        return output(myword.lower(), data[myword.lower()])
    elif  myword.upper() in data:
        return output(myword.upper(), data[myword.upper()])
    elif matchword(myword.lower()):
        myword = matchword(myword.lower())
        print('Did you mean ' + myword + '?')
        answer = input('yes/no ')
        if answer == 'yes':
            return output(myword, data[myword])
        else:
            inputword()
    else:
        return 'This word does not exist, please try again.'
print('bla')
myword = inputword()

