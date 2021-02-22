import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
import re
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from fuzzywuzzy import fuzz

import pymorphy2
# """
# Насколько слово близко к своей нормальной форме
# """

# morph = pymorphy2.MorphAnalyzer()
# a = morph.parse("красивейший")[0]
# print(fuzz.WRatio('красивейший', 'красиво'))
# print(fuzz.WRatio(a.normal_form, 'красиво'))
# print(a.normalized)

# """
# Здесь делится текст :
# на предложение при помощи метода '.tokensize'
# на слова при помощи метода '.wordtokensize'
# """
# nltk.download('punkt')
# text = 'Backgammon is one of the oldest known board games. Its history can be traced back nearly 5,000 y' \
#        'ears to archeological discoveries in the Middle East. It is a two player game where each player has fiftee' \
#        'n checkers which move between twenty-four points according to the roll of two dice.'
# sentences = nltk.sent_tokenize(text)
# for sentence in sentences:
#     words = nltk.word_tokenize(sentence)
#     print(words)
#     print()
# ---------------------------------------------------------------------------------------------------------------------------
"""
Здесь я применяю метода стеминга и лемматизации
Они приводят любую форму слова к дефолту 
Например: (собаки собаку собачка собачелла собачка)->собака
ЭТО ТОЛЬКО К АНГ СЛОВАМ, ДЛЯ РУУСКОГО Я БУДУ ЮЗАТЬ pymorph
"""
#
# nltk.download('wordnet')
#
#
# def compare_stemmer_and_lemmatizer(stemmer, lemmatizer, word, pos):
#     """
#     Print the results of stemmind and lemmitization using the passed stemmer, lemmatizer, word and pos (part of speech)
#     """
#     print("Stemmer:", stemmer.stem(word))
#     print("Lemmatizer:", lemmatizer.lemmatize(word, pos))
#     print()
#
#
# lemit = WordNetLemmatizer()
# word = ['женщину', 'папу', 'быстрый', 'собаки', 'собаку', 'гибкий']
# print(lemit.lemmatize('быстрый'))


# -----------------------------------------------------------------------------------------------------------------------
"""
Здесь мы находили стоп слова и убирали их 
Стопслова - это слова которые не несут смысловой нагрузки
"""

# nltk.download('stopwords')
# print(len(stopwords.words('russian')))
# stop_words = set(stopwords.words('russian'))
# sent = 'я ебал вашу политику лучше пусть он сам решает что и как делать же ну не надо ало дра блять я уебу тебе'
# words = nltk.word_tokenize(sent)
# without_stop_words = [word for word in words if not word in stop_words]
# print(without_stop_words)
"""
Здесь мы при помощи регулярных выражений убираем знаки препинания и подобное 
"""
# ----------------------------------------------------------------------------------------------------------------------


sentence = "The development!!!!!!!!!!!!###########@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$,,,,,,," \
           ",,,,,,,,,!!!!!!!!!!! of snowboarding was,,,,,,,,,,,,,,,,,,,,,,,,, inspired by skateboarding, sledding, surfing and skiing."
pattern = r"[^\w]"
print(re.sub(pattern, " ", sentence))
# -----------------------------------------------------------------------------------------------------------------------
spis = 'Я люблю смотреть фильмы и мне это нравится нравится нравится  я обожаю делать это. ' \
       'Вся моя семья смотрит это и радуется. Вся моя семья смотрит это и радуется.'
spis2 = spis[:]
spis = re.sub(pattern, ' ', spis)
stop_words = set(stopwords.words('russian'))
spis = nltk.word_tokenize(spis)

print(len(spis))
spis = [word for word in spis if not word in stop_words]
print(len(spis))


spis = set(spis)
print(len(spis))


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(spis)
feat_name = vectorizer.get_feature_names()
df = pd.DataFrame(X.toarray(), columns=feat_name)
print(df)
