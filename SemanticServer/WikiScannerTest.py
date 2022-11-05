import json
from WikiScanner import *

# data = []
# for i in range(1):
#     data += getSentences()
#
# with open("data.json", "w") as outfile:
#     json.dump(data, outfile)
# from simantic import WordProcessor
#
# with open('data.json', 'r') as openfile:
#     json_object = json.load(openfile)
#
# print(json_object)
# s = 0
# for i in json_object:
#     s += len(i)
# print(s)
#
from SemanticMeaningAnalyzer import SemanticMeaningAnalyzer
# dat = getSentencesLocal(r"C:\Users\u9146653\Downloads\he")
# dat += load_article(r"C:\Users\u9146653\Downloads\he\מ\ח\ש\מחשב.html")
#
# with open("data.json", "w") as outfile:
#     json.dump(dat, outfile)

with open('data.json', 'r') as openfile:
     dat = json.load(openfile)


w = SemanticMeaningAnalyzer(dat)
while(True):
    try:
        word = input()
        print(word)
        w.set_base_word(word)
        print(w.most_similar)
    except:
        print("not in vocab")

