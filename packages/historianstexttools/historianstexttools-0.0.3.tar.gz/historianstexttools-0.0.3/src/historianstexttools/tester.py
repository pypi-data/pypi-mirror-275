'''
import cleantext

print(cleantext.clean_text(['nltk@%,^rem""o""ve#!punTTTctualtion']))

print(cleantext.remove_stopwords(["I am just too cool for this I think!"]))

print(cleantext.remove_frequent_words(["I am just too cool for this I think!"], ["i", "am"]))

print(cleantext.lemmatize_text(["Ich habe zu viel zu tun.", 'Das ist sehr gut und viel besser!'], language='german'))
'''
'''
import chunk

docs = ['The story revolves around two brothers, Michael and Sam Emerson, who move with their recently divorced mother, Lucy, to the coastal town of Santa Carla, California, to live with their eccentric grandfather. Upon their arrival, they quickly realize that the town is plagued by mysterious disappearances and deaths.']

print(chunk.wordcount_chunking(documents=docs, chunk_size=10, overlap=2, break_at_sentence=True))

docs2 = ['Wie gehts! Ich heisse Christopher und ich bin 37 Jahre alt! Wie heisst du?', 'Klar! Ich bin Ben.']

print(chunk.sentence_chunking(docs2, 'german'))
'''

#print(cleantext.clean_text(['Hi! You are a great friend of mine!']))
import historianstexttools as htt
cleaning_docs = htt.HistoriansTextTools()
print(cleaning_docs.documents)
print(cleaning_docs.documents_without_punctuation)
print(cleaning_docs.documents_lemmatized)
print(cleaning_docs.documents_lowercased)
print(cleaning_docs.documents_cleaned)