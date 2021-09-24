import requests


# function to return a sentence for word passed to it

def sentence_generator(word):
    response = requests.get(
        f'https://lt-nlgservice.herokuapp.com/rest/english/realise?subject={word}&verb=eat&object=human')
    data = response.json()
    return data['sentence']
