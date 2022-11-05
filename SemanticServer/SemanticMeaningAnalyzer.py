from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count
import gensim.downloader as api

save_path = "model/model.dat"

class SemanticMeaningAnalyzer:
    def __init__(self, dataset=None, model=None):
        if model is not None:
            self.model = Word2Vec.load(model).wv
        else:
            if dataset is None:
                dataset = api.load("text8")
            self.data = [dat for dat in dataset]
            word2vec = Word2Vec(self.data, min_count=0, workers=cpu_count())
            word2vec.save(save_path)
            self.model = word2vec.wv
        self.base_word = ""

    def set_base_word(self, base_word):
        self.base_word = base_word
        self.most_similar = [word[0] for word in self.model.most_similar(base_word, topn=1000)]
        print(self.most_similar)

    def get_word_stats(self, word):
        position = -1
        if word in self.most_similar:
            position = self.most_similar.index(word)

        try:
            similarity = float(self.model.similarity(self.base_word, word))
        except:
            similarity = -1

        return {
            "similarity": similarity,
            "rank": 1000 - position
        }

