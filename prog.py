import json
from difflib import get_close_matches

# open and read json file
myfile = open('data.json')
data = json.load(myfile)
myfile.close()
# input word
def inputword():
    myword = input('Please enter the word: ')
    return myword.lower()
#  check if input match key for min 80%
def matchword(myword):
    match = get_close_matches(myword, data.keys(), n=1, cutoff = 0.8)
    if match !=[]:
        return match[0]
    else:
        return False
# return right answer
def translate(myword):
    if myword in data:
        str = 'The defenition of "{}": \n'.format(myword)
        for item in data[myword]:
            str = str + item +'\n'
        return str
    elif matchword(myword):
        myword = matchword(myword)
        print('Did you mean ' + myword + '?')
        answer = input('yes/no ')
        if answer == 'yes':
            return 'The defenition of {}: {}'.format(myword, data[myword])
        else:
            inputword()
    else:
        return 'This word does not exist, please try again.'

myword = inputword()
print(translate(myword))
