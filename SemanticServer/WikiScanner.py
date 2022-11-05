import urllib.request
import json
import requests
from bs4 import BeautifulSoup
import re
import os
from HebrewProcessor import HebrewProcessor

word_processor = HebrewProcessor()

def get_sentences_online():
    contents = urllib.request.urlopen("https://he.wikipedia.org/w/api.php?action=query&list=random&format=json&rnnamespace=0&rnlimit=1").read()
    data = json.loads(contents)
    url = "https://he.wikipedia.org/wiki/"+data["query"]["random"][0]["title"].replace(" ", "_")
    page = urllib.request.urlopen(str(url.encode("utf8"))[2:-1].replace("\\x", "%")).read()

    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')

    paragraphs = soup.findAll('p')
    sentences = []

    for i in paragraphs:
        for sentence in re.split('!|\.|:', i.getText()):
            if sentence.count(" ") >= 5:
                CHARS_PATTERN = re.compile(r"""[^אבגדהוזחטיכלמנסעפצקרשתןףץםך'\- "]""")
                sentence = CHARS_PATTERN.sub('', sentence)
                if sentence.find("   ") == -1:
                    result = sentence.split(" ")
                    if len(result) > 5:
                        sentences.append(result)
                        sentences[-1] = list(filter(lambda val: val != "", sentences[-1]))

    return sentences

def is_file_valid(name):
    FORBIDDEN = ["משתמש~", "שיחת_משתמש~", "תמונה~", "שיחה~"]
    for pat in FORBIDDEN:
        if pat in name:
            return False

    return True

def load_article(file_path):
    sentences = []
    try:
        html = open(file_path, "rb").read().decode('utf8')
        soup = BeautifulSoup(html, 'html.parser')
        f = [p.getText() for p in soup.find_all("p")]
        for p in soup.find_all('p'):
            if len(p.getText()) > 0 and len(re.sub("[^a-zA-Z]", "", p.getText())) / len(p.getText()) > 0.2:
                continue

            CHARS_PATTERN = re.compile(r"""[^אבגדהוזחטיכלמנסעפצקרשתןףץםך'\- "]""")
            sentence = CHARS_PATTERN.sub('', p.getText())
            if sentence.find("   ") == -1:
                result = sentence.split(" ")
                if len(result) > 5:
                    sentences.append([word_processor.process_word(word) for word in result if len(word) > 1])
                    #sentences.append(list(filter(lambda val: len(val) > 1, result)))

    except UnicodeDecodeError:
        return None

    if len(sentences) == 0:
        return None


    return sentences

def getSentencesLocal(path, fileCount = 120000):
    all_files = []
    for root, folders, filenames in os.walk(path):
        for filename in filenames:
            all_files.append(os.path.join(root, filename))

    all_files = list(filter(is_file_valid, all_files))

    sentences = []

    for i, file_path in enumerate(all_files[:fileCount]):
        print(i, fileCount)
        article_data = load_article(file_path)
        if article_data != None:
            sentences += article_data

    return sentences

