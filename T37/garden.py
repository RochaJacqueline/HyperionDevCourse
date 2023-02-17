import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

#doc = nlp("this is a test sentence")
#print([(w.text, w.pos_) for w in doc])
#displacy.serve(doc, style="ent")
#print([(i, i.label_, i.label) for i in doc.ents])

gardenpath_Sentences = ["The cotton clothing is made of grows in Mississippi.",
                       "The sour drink from the Atlantic.", 
                       "Mary gave the child the dog bit a BandAid.", 
                       "The Jewish man who whistles tunes pianos.",
                       "When John eats food gets thrown."]

docs = list(map(lambda s: nlp(s), gardenpath_Sentences))

# Does the tokenisation and prints labels for entities
for doc in docs:
    print([token.orth_ for token in doc if not token.is_punct | token.is_space])
    print([(i, i.label_, i.label) for i in doc.ents])

entity_GPE = spacy.explain("GPE")
print(f"Entity type 'GPE': {entity_GPE}")
# The entity GPE refers to contries, cities or states. Hence, it makes sense to be the label for Mississippi

entity_NORP = spacy.explain("NORP")
print(f"Entity type 'NORP': {entity_NORP}")
# The entity NORP refers to nationalities, religious or political groups. Its use is correct for Jewish 