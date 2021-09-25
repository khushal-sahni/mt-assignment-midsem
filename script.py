import requests

from delphin import ace
## function to return a sentence for word passed to it 

def sentenceGenerator(word):
    response = requests.get(f'https://lt-nlgservice.herokuapp.com/rest/english/realise?subject={word}&verb=eat&object=human')

    data = response.json()
    return data['sentence']


def aceParser(sentence):
    response = ace.parse('erg-1214-x86-64-0.9.24.dat', sentence, executable = './ace-0.9.24/ace')
    return response['results'][0]['mrs']

def doSomething(word):
    sentence = sentenceGenerator(word)
    aceParse = aceParser(sentence)
    length = len(word)
    pos = aceParse.find(f'<4:{4+length}')  # position of that <4:20> kinda thing

    pos1 = pos;
    while(aceParse[pos1-1] != ' '):
        pos1 -= 1
    mrs = aceParse[pos1 : pos]
    print(mrs) 

    pos2 = pos
    while(aceParse[pos2] != ' '):
        pos2 += 1
    pos2 += 1
    pos3 = pos2
    while(aceParse[pos3] != ']'):
        pos3 += 1
    pos3 -= 1
    concept_label = aceParse[pos2 : pos3]
    print(concept_label)

doSomething("fuck")

