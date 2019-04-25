import prepocess
import time
from gensim.models import Word2Vec

class word2vec():
    def __init__(self):
        self.w2v_model = None

    def get_embeddings(self):
        embeddings = {}
        
        for k in self.w2v_model.wv.vocab:
            embeddings[k] = self.w2v_model[k]
        return embeddings

    def get_vectors(self, sentences):
        all_vectors = []

        embedding_dim = self.w2v_model.vector_size
        embedding_unknown = [0 for i in range(embedding_dim)]

        for sentence in sentences:
            this_vector = []
            for word in sentence:
                if word in self.w2v_model.wv.vocab:
                    this_vector.append(self.w2v_model[word])
                else:
                    this_vector.append(embedding_unknown)
            all_vectors.append(this_vector)

        return all_vectors

    def train(self, sentences, embedding_size=128, window=5, min_count=2):
        begin = time.time()
        self.w2v_model = Word2Vec(sentences, size = embedding_size, window = window, min_count = min_count)
        end = time.time()
        print("train time: {} seconds".format(end - begin))

    def save(self, file_to_save='./data/word_embedding'):
        self.w2v_model.save(file_to_save)
        print('save file to {}'.format(file_to_save))

    def load(self, file_to_load='./data/word_embedding'):
        self.w2v_model = Word2Vec.load(file_to_load)
        print('load file from {}'.format(file_to_load))

    def most_similar(self, word):
        return self.w2v_model.most_similar(word)

    def most_similar_advance(self, positive, negative, topn=10):
        return self.w2v_model.most_similar(positive, negative, topn)

    def cal_similarity(self, word1, word2):
        return self.w2v_model.similarity(word1, word2)

    def doesnt_match(self, words):
        return self.w2v_model.doesnt_match(words)


if __name__ == '__main__':
    # load text and label
    sentences = prepocess.load_positive_negative_data_files('./data/corpus10000.utf8')

    model = word2vec()
    # train and save
    model.train(sentences)
    model.save()
    
    # load
    #model.load()
    embeddings = model.get_embeddings()
    
    print(embeddings['我'])

    print(model.most_similar('我'))
    print(model.most_similar_advance(['我'], ['你']))

    print(model.cal_similarity('我', '我们'))
    print(model.doesnt_match(['我', '不', '爱', '你']))






