import spacy
from spacy.matcher import PhraseMatcher
import pandas as pd
import plac
from pathlib import Path
import random


from com.util.ResourceConfig import *


def offseter(lbl, doc, match_item):
    o_one = len(str(doc[0:match_item[1]]))
    sub_doc = doc[match_item[1]:match_item[2]]
    o_two = o_one + len(str(sub_doc))
    return (o_one, o_two, lbl)


'''nlp = spacy.load('en')

if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner)
else:
    ner = nlp.get_pipe('ner')'''

# file = open("/Users/v.bq.kumar/vijay/python_projects/com/test_data.txt", "r")
# to_analyse = file.read()


##with open("/Users/v.bq.kumar/vijay/python_projects/com/test_data.txt") as fileStream:
##line = True

##while line:
##line = fileStream.readline()

def find_data(line):
    initialize()
    return get_response(line)


to_analyse = 'hello'
print(find_data(to_analyse))
# print(start + end)

'''to_analyse = ('Hello Code & Supply, '
              'my name is Vijay and tonight '
              'we\'re in Bangalore')

doc = nlp(to_analyse)
ents = [(x.text, x.label_) for x in doc.ents]
print(ents)'''
