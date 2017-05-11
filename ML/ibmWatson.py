import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as features

nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2017-05-11',
                                                            username='92475337-a51a-47f2-b42e-69e772b1e3cc',
                                                            password='NdHjAGCYDeOf')
# # SENTIMENTS FOR QUESTIONS
sentimentOutput = nlu.analyze(text='What is the best course in Columbia computer science?',
            features=[features.Sentiment()])
print(sentimentOutput)
# #{'sentiment': {'document': {'label': 'neutral', 'score': 0.0}}, 'language': 'en'}

# # CATEGORIES FOR QUESTIONS
# # CAN THEN GROUP SIMILAR QUESTIONS
categoryOutput = nlu.analyze(text='What is the best course in Columbia computer science?',
            features=[features.Categories()])
print(categoryOutput)
# # {'categories': [{'label': '/science/computer science', 'score': 0.954436}, {'label': '/business and industrial/aerospace and defense/space technology', 'score': 0.214094}, {'label': '/education/graduate school/college', 'score': 0.151691}], 'language': 'en'}


# # KEYWORDS / TAGS FOR QUESTIONS
keywordOutput = nlu.analyze(text='What is the best course in Columbia computer science?',
            features=[features.Keywords()])
print(keywordOutput)
# # {'keywords': [{'text': 'best course', 'relevance': 0.928725}, {'text': 'Columbia computer science', 'relevance': 0.907045}], 'language': 'en'}

# CONCEPTS FOR QUESTIONS
conceptOutput = nlu.analyze(text='What is the best course in Columbia computer science?',
            features=[features.Concepts()])
# {'concepts': [{'relevance': 0.911116, 'dbpedia_resource': 'http://dbpedia.org/resource/Computer_science', 'text': 'Computer science'}, {'relevance': 0.832372, 'dbpedia_resource': 'http://dbpedia.org/resource/Computational_science', 'text': 'Computational science'}], 'language': 'en'}


# When posting a question, run categories, keywords, and concepts.
# Choose one from each if not duplicate.