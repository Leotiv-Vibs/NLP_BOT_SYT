from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
import pymorphy2
import re
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('stopwords')
morph = pymorphy2.MorphAnalyzer()
stop_words = set(stopwords.words('russian'))

opts = {"alias": ('pythonguru', 'пайтонгуру', 'гурупайтон', 'pythonguru', 'пайтон гуру', 'гуру пайтон'),
        "tbr": (
            'скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как', 'расскажи', 'сколько', 'поставь', 'переведи',
            "засеки", "рассказать"
                      'запусти', 'сколько будет', 'мне', 'нам', 'ему', 'свою', 'лучшую',),
        "sign": ('.', ')', '(', '!', '?', '/', '\\', ',', '#', '@', '\'', '\"', '%'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время', 'какое сейчас время'),
             'startStopwatch': ('запусти секундомер', "включи секундомер", "засеки время"),
             'stopStopwatch': ('останови секундомер', "выключи секундомер", "останови"),
             "stupid1": (
                 'расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты', "шутка", "прикол", "историю", 'сказку'),
             "calc": ('прибавить', 'умножить', 'разделить', 'степень', 'вычесть', 'поделить', 'х', '+', '-', '/'),
             "shutdown": ('выключи', 'выключить', 'отключение', 'отключи', 'выключи компьютер'),
             "conv": ("валюта", "конвертер", "доллар", 'руб', 'евро'),
             "internet": ("открой", "вк", "гугл", "сайт", 'вконтакте', "ютуб"),
             "translator": ("переводчик", "translate"),
             "deals": ("дела", "делишки", 'как сам', 'как дела')}}


def callback():
    cmd = input().lower()

    for x in opts['alias']:
        cmd = cmd.replace(x, " ").strip()
    for x in opts['tbr']:
        cmd = cmd.replace(x, " ").strip()
    for x in opts['sign']:
        cmd = cmd.replace(x, '').strip()
    cmd = cmd.replace('рас', '')
    cmd = nltk.sent_tokenize(cmd)

    words = list()
    for i in cmd:
        words.append(nltk.word_tokenize(i))

    words_morph = []
    for i in words:
        for j in i:
            words_morph.append(morph.parse(j)[0].normal_form)

    cmd = [word for word in words_morph if not word in stop_words]
    print(cmd)
    return cmd


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 50}
    for c, v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.WRatio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
                print(c, vrt)
            else:

                return 'Очень интересно, давай сменим тему'
    return RC


recognize_cmd(callback())
