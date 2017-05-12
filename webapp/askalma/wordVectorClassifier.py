from gensim.models import word2vec
import pickle

# http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/
# Our Model: 200 features (each hidden layer has 200 columns in weight matrix)
#	For each hidden neuron, node has 250,000 by 200 matrix
# Model calculates for each word, probability of each other word
# Skip Gram Neural Network
# Train on text8 (Wikipedia dump): 253,855 unique words, 17,005,208 total words

"""
Input: contents, Action: Dump into pickle file called Classifier.pkl
"""
def dumpIntoPickle(contents):
	with open('WordVectorPickle.pkl', 'wb') as f:
		pickle.dump(contents, f, protocol=2)

"""
Input: pickle file, Return: contents of file
"""
def loadPickleFile(pickleFile):
	with open(pickleFile, "rb") as f:
		data = pickle.load(f)
	return data

def machineLearning(search):
	# model = loadPickleFile("WordVectorPickle.pkl")
	model = word2vec.Word2Vec.load("WordVecModel")

	# Can use for recommended tags / good
	return model.most_similar([search])