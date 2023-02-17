# Compulsory task 1

import spacy

nlp = spacy.load("en_core_web_sm")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
# Cat is more similar to monkey, than banana is to monkey. Still, the least similar is banana and cat.
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

""" When using the simpler language model (en_core_web_sm), the percentages of similarity are different. The console shows a user warning,
since this model does not have word vectors and the similarity might not be useful as when using the model en_core_web_md.
"""