def add_entries_to_h_concept_and_mrs(h_concept_path, mrs_rel_path, word_wx, word_meaning, mrs, mrs_rel):
    word_count = 0
    meaning_count = 0
    is_mrs_found = False

    with open(h_concept_path, 'r+') as file_data:
        tokenized = file_data.read().split()
        for word in tokenized:
            if word == mrs + ')':
                is_mrs_found = True
            if word.startswith(word_wx + '_'):
                word_count = max(int(word.split('_')[1]), word_count)
            if word.startswith(word_meaning + '_'):
                meaning_count = max(int(word.split('_')[1]), meaning_count)

        to_be_write = '(concept_label-concept_in_Eng-MRS_concept ' + word_wx + '_' + str(
            word_count) + ' ' + word_meaning + '_' + str(meaning_count) + ' ' + mrs + ')'
        file_data.write('\n' + to_be_write)

    if not is_mrs_found:
        with open(mrs_rel_path, 'a') as file_data:
            to_be_write = '(MRS_concept-label-feature_values ' + mrs + ' LBL: ' + mrs_rel + ')'
            file_data.write('\n' + to_be_write)