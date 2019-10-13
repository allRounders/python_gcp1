import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en')
matcher = PhraseMatcher(nlp.vocab)
data = pd.read_csv('/Users/v.bq.kumar/vijay/python_projects/resources/CC_Label_data.csv', encoding='utf-8')


def initialize():
    for item in data.values:
        for values in str(item[1]).split(','):
            matcher.add(str(item[0]), None, nlp(values.strip().lower()))

    return matcher


def get_response(message_text):
    doc = nlp(str(message_text).lower())
    matches = matcher(doc)
    flag = True
    response = ""
    priority = -1
    for match, start, end in matches:
        span = doc[start:end]
        string_id = nlp.vocab.strings[match]
        for item in data.values:
            if string_id == item[0] and (response == "" or int(item[3]) >= priority):
                response = str(item[2]).replace('{item}', span.text)

    return response
