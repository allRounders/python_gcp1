import nltk.tag
from nltk import word_tokenize, PerceptronTagger, ne_chunk
from nltk.corpus import *
from nltk import *


class MyCustomTagger:
    def __init__(self):
        self._taggers = [PerceptronTagger()]


label = {'president': 'NNP', 'white house': 'NNP'}
tagger = nltk.tag.UnigramTagger(model=label, backoff=MyCustomTagger())

NE_token1 = ['president', 'white house']
NE_tags = tagger.tag(NE_token1)
NE_ner = ne_chunk(NE_tags)
# print(NE_ner)

def lang_ratio(input):
    lang_ratio = {}
    tokens = wordpunct_tokenize(input)
    print("tokens=" + str(tokens))
    words = [word.lower() for word in tokens]
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        lang_ratio[language] = len(common_elements)
    return lang_ratio


def detect_language(input):
    ratios = lang_ratio(input)
    language = max(ratios, key=ratios.get)
    return language


inputs = ["hola mi nombre es Tony Cruz", 'The US President stays in the White House', 'The China President Xin Ping']

for input in inputs:
    print(detect_language(input))
    '''if detect_language(input) == 'english':
        NE_token = word_tokenize(input)
        NE_tags = nltk.pos_tag(NE_token)
        print(NE_tags)
        #NE_ner = ne_chunk(NE_tags)
        #print(NE_ner)'''

