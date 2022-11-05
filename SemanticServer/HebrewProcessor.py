# -*- coding: utf-8 -*-
import json
import re
import os

DEFULT_WORD_FILES = [r"./he-data/nouns.txt", r"./he-data/verbs.txt"]

def create_dict(files):
    word_dict = {}
    key_words = set()
    CHARS_PATTERN = re.compile(r"""[^אבגדהוזחטיכלמנסעפצקרשתןףץםך"]""")
    for file_name in files:
        with open(file_name, 'r', encoding="utf-8") as file:
            file_text = file.read()
            word_sections = [l for l in file_text.split("\n-") if l != []]
            for word_types in word_sections:
                word_types_arr = word_types.split("\n")
                word_types_arr = [CHARS_PATTERN.sub('', word) for word in word_types_arr if CHARS_PATTERN.sub('', word) != ""]
                if len(word_types_arr):
                    base_word = word_types_arr[0]
                    key_words.add(base_word)
                    for word in word_types_arr:
                        if word not in key_words and word not in word_dict or word == base_word:
                            word_dict[word] = base_word

    return word_dict

def write_dict_to_file(dict_name, files):
    with open(dict_name, "w") as outfile:
        word_dict = create_dict(files)
        json.dump(word_dict, outfile)


class HebrewProcessor:
    def __init__(self, files = DEFULT_WORD_FILES):
        self.word_dict = create_dict(files)

    def process_word(self, word):
        PREFIXES = ["ו", "ה", "ב", "ש", "כ", "ל", "מ", "מה", "מש", "וה", "וש", "ומ", "ול", "וב"]

        if word in self.word_dict:
            return self.word_dict[word]

        for pref in PREFIXES:
            no_pref = word[word.startswith(pref) and len(pref):]
            if no_pref in self.word_dict:
                return self.word_dict[no_pref]

        return word
