import urllib.request
import json
import requests
from bs4 import BeautifulSoup
import re
import random
from HebrewProcessor import HebrewProcessor

def getSentences():
    contents = urllib.request.urlopen("https://he.wikipedia.org/w/api.php?action=query&list=random&format=json&rnnamespace=0&rnlimit=1").read()
    data = json.loads(contents)
    #print(data["query"]["random"][0]["title"])
    url = "https://he.wikipedia.org/wiki/"+data["query"]["random"][0]["title"].replace(" ", "_")
    #print(str(url.encode("utf8"))[2:-1].replace("\\x", "%"))
    page = urllib.request.urlopen(str(url.encode("utf8"))[2:-1].replace("\\x", "%")).read()
    #print(urllib.request.urlopen(str(url.encode("utf8"))[2:-1].replace("\\x", "%")).read())

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

r_w = ["ילד","חתול", "חולצה", "מים", "רעש", "מכונית", "חייזרים"]

def solve(base):
    wiki_url = "https://he.wikipedia.org/wiki/" + base
    best_url = r"https://semantle-he.herokuapp.com/api/distance?word=" + base
    best_result = json.load(urllib.request.urlopen(str(best_url.encode("utf8"))[2:-1].replace("\\x", "%")))
    last_url = ""
    print(best_result)
    done = set()
    hebrew_proc = HebrewProcessor()

    while True:
        if wiki_url == last_url:
            wiki_url = "https://he.wikipedia.org/wiki/" + random.choice(r_w)
        last_url = wiki_url
        html_page = requests.get(wiki_url).content
        soup = BeautifulSoup(html_page, 'html.parser')

        paragraphs = soup.findAll('p')
        for p in paragraphs:
            out = False
            for word in p.getText().split(" "):
                try:
                    CHARS_PATTERN = re.compile(r"""[^אבגדהוזחטיכלמנסעפצקרשתןףץםך]""")
                    n_w = CHARS_PATTERN.sub('', word)
                    n_w = hebrew_proc.process_word(n_w)
                    if n_w in done:
                        continue
                    done.add(n_w)
                    print(n_w)

                    try_url = r"https://semantle-he.herokuapp.com/api/distance?word=" + n_w
                    result = json.load(urllib.request.urlopen(str(try_url.encode("utf8"))[2:-1].replace("\\x", "%")))
                    print(result)
                    print("best: ", best_result)
                    if result['similarity'] > best_result['similarity']:
                        print("-------------------------")
                        best_result = result
                        best_url = try_url
                        wiki_url = "https://he.wikipedia.org/wiki/" + word
                        out = True
                        break
                except:
                    pass
            if out:
                break



