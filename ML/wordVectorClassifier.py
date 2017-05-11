from gensim.models import word2vec

# http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/
# Our Model: 200 features (each hidden layer has 200 columns in weight matrix)
#	For each hidden neuron, node has 250,000 by 200 matrix
# Model calculates for each word, probability of each other word
# Skip Gram Neural Network
# Train on text8 (Wikipedia dump): 253,855 unique words, 17,005,208 total words

# sentences = word2vec.Text8Corpus('text8')
# model = word2vec.Word2Vec(sentences, size=200)
# model.save("WordVecModel")
model = word2vec.Word2Vec.load("WordVecModel")

# Can use for recommended tags / good
print(model.most_similar(['technology']))

# Can use for similarity detection among questions / Not that accurate
print(model.similarity('technology', 'computer'))
