from locale import Error
import requests

from delphin import ace


# function to return a sentence for word passed to it

def sentenceGenerator(word, type="subject"):
    if (type == "subject"):
        response = requests.get(
            f'https://lt-nlgservice.herokuapp.com/rest/english/realise?subject={word}&verb=eat&object=human')
    elif (type == "verb"):
        response = requests.get(
            f'https://lt-nlgservice.herokuapp.com/rest/english/realise?subject=dog&verb={word}&object=human')
    elif (type == "object"):
        response = requests.get(
            f'https://lt-nlgservice.herokuapp.com/rest/english/realise?subject=dog&verb=eat&object={word}')
    elif (type == "adjective"):
        response = requests.get(
            f'https://lt-nlgservice.herokuapp.com/rest/english/realise?subject=dog&verb=eat&object=human&objmod={word}')
    else:
        raise Error("PLease pass correct type value")
    data = response.json()
    return data['sentence']


def aceParser(sentence, compiled_grammer_path, ace_binary_path):
    response = ace.parse(compiled_grammer_path, sentence, executable=ace_binary_path)
    print(len(response['results']))
    if len(response['results']) > 0:
        return response['results'][0]['mrs']
    else:
        return 0


def doSomething(word, type="subject"):
    sentence = sentenceGenerator(word, type)
    aceParse = aceParser(sentence)
    wordIndex = sentence.find(word)
    length = 0
    while (sentence[wordIndex + length] != ' '):
        length += 1
    pos = aceParse.find(f'<{wordIndex}:{wordIndex + length}')  # position of that <4:20> kinda thing

    pos1 = pos;
    while (aceParse[pos1 - 1] != ' '):
        pos1 -= 1
    mrs = aceParse[pos1: pos]
    print(mrs)

    pos2 = pos
    while (aceParse[pos2] != ' '):
        pos2 += 1
    pos2 += 1
    pos3 = pos2
    while (aceParse[pos3] != ']'):
        pos3 += 1
    pos3 -= 1
    concept_label = aceParse[pos2: pos3]
    print(concept_label)


