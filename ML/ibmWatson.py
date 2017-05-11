import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as features

nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2017-05-11',
                                                            username='92475337-a51a-47f2-b42e-69e772b1e3cc',
                                                            password='NdHjAGCYDeOf')
# SENTIMENTS FOR QUESTIONS
output = nlu.analyze(text='this is my experimental text.  Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne.',
            features=[features.Sentiment()])

# CATEGORIES FOR QUESTIONS
# CAN THEN GROUP SIMILAR QUESTIONS
output = nlu.analyze(text='this is my experimental text.  Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne.',
            features=[features.Categories()])
# {'language': 'en', 'categories': [{'score': 0.677258, 'label': '/art and entertainment/movies and tv/movies'}, {'score': 0.447564, 'label': '/technology and computing/software/graphics software'}, {'score': 0.337757, 'label': '/business and industrial/biomedical'}]}

# KEYWORDS / TAGS FOR QUESTIONS
output = nlu.analyze(text='this is my experimental text.  Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne.',
            features=[features.Keywords()])

print(output)
