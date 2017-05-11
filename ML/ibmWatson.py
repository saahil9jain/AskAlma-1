import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as features

nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2017-05-11',
                                                            username='92475337-a51a-47f2-b42e-69e772b1e3cc',
                                                            password='NdHjAGCYDeOf')
output = nlu.analyze(text='this is my experimental text.  Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne.',
            features=[features.Sentiment()]) #select features.Categories() to get categories
print(output)
