import re
import nltk.corpus
from nltk import word_tokenize, FreqDist, ne_chunk
from nltk.corpus import stopwords, movie_reviews
from nltk.stem import PorterStemmer
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer

import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB, MultinomialNB
import nltk.tag
import nltk.data

# print(os.listdir(nltk.data.find("corpora")))

AI = """In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, 
in contrast to the natural intelligence displayed by humans. Leading AI textbooks define the field as the study of "intelligent agents": 
any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[1] Colloquially, 
the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate
 with the human mind, such as "learning" and "problem solving".[2] As machines become increasingly capable, tasks considered to require 
 "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.[3] A quip in Tesler's Theorem says 
 "AI is whatever hasn't been done yet."[4] For instance, optical character recognition is frequently excluded from things considered to be AI, 
 having become a routine technology.[5] Modern machine capabilities generally classified as AI include successfully understanding human speech,
 [6] competing at the highest level in strategic game systems (such as chess and Go),[7] autonomously operating cars, intelligent routing in 
 content delivery networks, and military simulations."""

AI_tokens = word_tokenize(AI)

fdist = FreqDist()

for word in AI_tokens:
    fdist[word.lower()] += 1

fdist_top10 = fdist.most_common(10)

quotes = "The best and most beautifule things in the world cannot be seen or veven touched, they must be felt with " \
         "the heart. "

quotes_tokens = nltk.word_tokenize(quotes)
# print(quotes_tokens)

quotes_bigrams = list(nltk.bigrams(quotes_tokens))
# print(quotes_bigrams)

quotes_trigrams = list(nltk.trigrams(quotes_tokens))
# print(quotes_trigrams)

quotes_ngrams = list(nltk.ngrams(quotes_tokens, 4))
# print(quotes_ngrams)

pst = PorterStemmer()
result1 = pst.stem('having')
# print(result1)

word_lem = WordNetLemmatizer()
# print(word_lem.lemmatize('corpora'))

words_to_stem = ['give', 'given', 'giving', 'gave']

# for words in words_to_stem:
# print(words + ":" + word_lem.lemmatize(words))

# print(stopwords.words('english'))
# print(len(stopwords.words('english')))

# print(fdist_top10)

punctuation = re.compile(r'[-.?!,:;()|0-9]')

post_punctuations = []
for words in AI_tokens:
    word = punctuation.sub("", words)
    if len(word) > 0:
        post_punctuations.append(word)

# print(post_punctuations)

sentnc2 = "Vijay is natural when it comes to drawing"
sent2_tokens = word_tokenize(sentnc2)
# for token2 in sent2_tokens:
# print(nltk.pos_tag([token2]))

sentnc3 = "jai is eating a delicious cake"
sent3_tokens = word_tokenize(sentnc3)
# for token3 in sent3_tokens:
# print(nltk.pos_tag([token3]))

NE_sent = "The US president stays in the white house"
NE_token = word_tokenize(NE_sent)
NE_tags = nltk.pos_tag(NE_token)
NE_ner = ne_chunk(NE_tags)
print(NE_ner)


NE_sent1 = "The US President stays in the White House"
NE_token1 = word_tokenize(NE_sent1)
NE_tags1 = nltk.pos_tag(NE_token1)
NE_ner1 = ne_chunk(NE_tags1)
print(NE_ner1)

'''
#print(movie_reviews.categories())
# print(movie_reviews.fileids('pos'))

# rev = movie_reviews.words('pos/cv000_29590.txt')
# print(rev)

rev_list = []

neg_rev = movie_reviews.fileids('neg')
for rev in neg_rev:
    rev_text_neg = rev = movie_reviews.words(rev)
    rev1 = " ".join(rev_text_neg)
    rev1 = rev1.replace(' ,', ',')
    rev1 = rev1.replace(' .', '.')
    rev1 = rev1.replace('\' ', '')
    rev1 = rev1.replace(' \'', '')
    rev_list.append(rev1)

pos_rev = movie_reviews.fileids('pos')
for rev in pos_rev:
    rev_text_pos = rev = movie_reviews.words(rev)
    rev2 = " ".join(rev_text_pos)
    rev2 = rev2.replace(' ,', ',')
    rev2 = rev2.replace(' .', '.')
    rev2 = rev2.replace('\' ', '')
    rev2 = rev2.replace(' \'', '')
    rev_list.append(rev2)

# print(len(rev_list))


neg_targets = np.zeros((1000,), dtype=np.int)
pos_targets = np.ones((1000,), dtype=np.int)

target_list = []
for neg_tar in neg_targets:
    target_list.append(neg_tar)

for pos_tar in pos_targets:
    target_list.append(pos_tar)

# print(len(target_list))

y = pd.Series(target_list)

# print(y.head())

count_vect = CountVectorizer(lowercase=True, stop_words='english', min_df=2)
x_count_vect = count_vect.fit_transform(rev_list)
# print(x_count_vect.shape)

x_names = count_vect.get_feature_names()
# print(x_names)

x_count_vect = pd.DataFrame(x_count_vect.toarray(), columns=x_names)
print(x_count_vect.head())

x_train_cv, x_test_cv, y_train_cv, y_test_cv = train_test_split(x_count_vect, y, test_size=0.25, random_state=5)

gnb = GaussianNB()
y_pred_gnb = gnb.fit(x_train_cv, y_train_cv).predict(x_test_cv)

clf_cv = MultinomialNB()
clf_cv.fit(x_train_cv, y_train_cv)

y_pred_cv = clf_cv.predict(x_test_cv)

print("accuracy_score=" + str(metrics.accuracy_score(y_test_cv, y_pred_cv)))

score_clf_cv = confusion_matrix(y_test_cv, y_pred_cv)
print(score_clf_cv)'''
