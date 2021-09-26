from googletrans import Translator
from wxconv import WXC
from nltk.corpus import wordnet

translator = Translator()


def wx_converter(word):
    con = WXC(order='utf2wx')
    return con.convert(word)


def hindi_to_english(word):
    meaning = translator.translate(word, dest='en')
    return meaning.text


def sentence_generator(word):
    syns = wordnet.synsets(word)
    if len(syns) == 0:
        return 0
    if len(syns[0].examples()) > 0:
        return syns[0].examples()[0]
    else:
        return 0


def get_mrs_concept_and_rels(word_start_pos, word_end_pos, mrs):
    pos = mrs.find('<' + str(word_start_pos) + ':' + str(word_end_pos) + '>')
    mrs_start = pos
    while mrs[mrs_start] != '[':
        mrs_start = mrs_start - 1
    mrs_concept = mrs[mrs_start + 1:pos]
    print(mrs)
    print(pos)
    print('-----------------------')
    return mrs_concept
