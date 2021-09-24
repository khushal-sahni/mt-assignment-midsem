import requests

from delphin import ace
## function to return a sentence for word passed to it 

def sentenceGenerator(word):
    response = requests.get(f'https://lt-nlgservice.herokuapp.com/rest/english/realise?subject={word}&verb=eat&object=human')

    data = response.json()
    return data['sentence']


def aceParser(sentence):
    response = ace.parse('erg-1214-x86-64-0.9.24.dat', sentence, executable = './ace-0.9.24/ace')
    print(response['results'][0]['mrs'])

