# -*- coding: utf-8 -*-
import json

from flask import Flask
from flask import jsonify
from SemanticMeaningAnalyzer import SemanticMeaningAnalyzer
from HebrewProcessor import HebrewProcessor
from datetime import datetime, timezone, timedelta


def get_time():
    time = datetime.now() - timedelta(days=1)
    time = time.replace(hour=21, second=0, minute=0, microsecond=0)
    return int((time - datetime(1970, 1, 1)).total_seconds() * 1000)

def create_app(data_set_path=None, model_path=None):
    app = Flask("my_app")

    if model_path:
        semantic_meaning_analyzer = SemanticMeaningAnalyzer(model=model_path)
    elif data_set_path:
        with open(data_set_path, 'r') as openfile:
            data_set = json.load(openfile)
        semantic_meaning_analyzer = SemanticMeaningAnalyzer(data_set)
    else:
        semantic_meaning_analyzer = SemanticMeaningAnalyzer()

    hebrew_processor = HebrewProcessor()
    semantic_meaning_analyzer.set_base_word("מחשב")

    @app.route('/test/<string:word>')
    def test_word(word):
        word = hebrew_processor.process_word(word)
        result = semantic_meaning_analyzer.get_word_stats(word)
        result["time"] = get_time()
        return jsonify(result)

    return app
