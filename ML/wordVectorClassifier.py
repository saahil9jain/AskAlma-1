from gensim.models import word2vec

# sentences = [['first', 'sentence'], ['second', 'sentence']]
# sentences = word2vec.Text8Corpus('text8')
# model = word2vec.Word2Vec(sentences, size=200)
# model.save("WordVecModel")
model = word2vec.Word2Vec.load("WordVecModel")

# Can use for recommended tags / relatively good
print(model.most_similar(['technology']))

# Can use for similarity detection among questions / Not that accurate
print(model.similarity('bathroom', 'restroom'))
