from wordnet import word_net

from scrape import scrape_webpage_get_words
from script import aceParser
from util import hindi_to_english, sentence_generator, wx_converter, get_mrs_concept_and_rels

total_page = 709

ace_binary_path = '/home/kishan/ace-0.9.24/ace'
compiled_grammer_path = '/home/kishan/ace-0.9.24/erg-1214-x86-64-0.9.24.dat'

for i in range(total_page):
    words_list = scrape_webpage_get_words(i + 1)
    words_english = [hindi_to_english(word) for word in words_list]
    for word in words_english:
        if len(word.split()) > 1:
            continue
        sentence = sentence_generator(word)
        if sentence == 0:
            continue
        wx_notation = wx_converter(word)
        print(sentence)
        mrs = aceParser(sentence, compiled_grammer_path, ace_binary_path)
        if mrs == 0:
            continue
        word_start_pos = sentence.find(word)
        word_end_pos = word_start_pos + len(word) - 1
        mrs_concept = get_mrs_concept_and_rels(word_start_pos, word_end_pos, mrs)
        print(mrs_concept)
