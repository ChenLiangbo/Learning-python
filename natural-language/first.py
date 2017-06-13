#!usr/bin/env/python 
# -*- coding: utf-8 -*-

# python自然语言处理 
# book demo,example
# anaconda ,python 3.5

import nltk
# nltk.download()
# nltk.corpus.gutenberg.fileids()
# from nltk.book import text4

# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
# print(dir(text4))

# text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
# print("text = ",text,nltk.pos_tag(text))

import random
from nltk.corpus import names

def gender_features(word):
    return {'last_letter': word[-1]}


names = ([(name, 'male') for name in names.words('male.txt')] + 
	     [(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)
print(len(names))
print(names[0:10])
featuresets = [(gender_features(n), g) for (n,g) in names]

train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

classifier.classify(gender_features('Neo'))
classifier.classify(gender_features('Trinity'))

print(nltk.classify.accuracy(classifier, test_set))

classifier.show_most_informative_features(5)