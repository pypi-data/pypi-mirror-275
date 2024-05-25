import xml.etree.ElementTree as ET
import corpusparser

filename = 'tests/data/Melusine.xml'
format = 'colmep'
d = corpusparser.Document.create_from_nonstandard_file(filename, format)
d.set_id('ARTHUR')

print('Number of words: ', d.count_words())
print('Most frequent words: ', d.word_frequency_no_punctuation().most_common(30))
print('Most frequent punctuation: ', d.word_frequency_contains_punctuation().most_common(30))


# # print(d.tag)
d.transform_tokenise_sentences(tokenisation_model="period_and_capital")
d.transform_common_spellings()
d.update_spellings('ħ', 'h')
d.update_spellings('þ', 'th')

print('Number of words: ', d.count_words())
print('Number of sentences: ', d.count_sentences())
print('Longest sentence: ', d.longest_sentence_length())
print('Shortest sentence: ', d.shortest_sentence_length())
print('Average sentence length: ', d.average_sentence_length())

print('Most frequent words: ', d.word_frequency_no_punctuation(correctedText=True).most_common(30))
print('Most frequent punctuation: ', d.word_frequency_contains_punctuation(correctedText=True).most_common(30))
print("XML tags: ", d.get_xml_tags())


out_file = 'tests/data/Melusine-output.xml'
d.to_xml_file(out_file, indent=2)

sents = d.get_sentences_as_text_list(correctedText=True)
sents_filename = "tests/data/Melusine-sentences.txt"
try:
    with open(sents_filename, 'w') as f:
        for s in sents:
            f.write(f"{s}\n")
except IOError:
    print("IOError: Could not write to file " + sents_filename)


# # NB make sure to update spellings before adding text to sentences
# d.transform_remove_asterisks()
# d.transform_v_to_u()
# d.transform_u_to_v()
# d.transform_ye_caret_to_the()
# d.transform_add_convenience_text_to_sentences()
# d.transform_number_sentences()
# # d.transform_parse(add_parse_string=True, restructure=True, id=d.get_id())
# # d.transform_pos_tag(id=d.get_id())
# d.print_info()

# get sentences
# sents = d.get_sentences()
# s = sents[0]
# s.parse(add_parse_string=True, restructure=True)
# sents = d.get_sentences_as_text_list()
# for s in sents:
#     print(s, '\n')

# print the first part of the XML to check
# xml = d.to_xml_string(indent=4)
# print(xml[:12000])
# print('Sentences :', d.get_sentence_count())
# sent_e = d.get_sentences_as_elements()
# s = Sentence.create_from_element(sent_e[0])
# t = s.get_attribute('conv-text')
# print(t)
# e = d.get_underlying_element()
# l = list(e.iter('w'))
# print(l[:10])
# print('Words     :', d.get_word_count())
# print('Longest   :', d.get_longest_sentence())
# print('Shortest  :', d.get_shortest_sentence())
# print('Average   :', d.get_average_sentence_length())
# print(d.word_frequency_starts_with('w'))
# print(d.word_frequency_contains_punctuation())
# print(d.get_xml_tags())

# sents = d.get_sentences_as_elements()
# # check this is the right size
# print(len(sents))
# # check we can create Sentence objects
# s = Sentence.create_from_element(sents[2])
# t = s.get_attribute('conv-text')
# print(t[:18])

# write to file
# out_file = 'tests/data/output.xml'
# d.to_xml_file(out_file, indent=2)

# conc = d.concordance_in(['which', 'whiche', 'whyche'], separator='@')
# for c in conc:
#     print(c)