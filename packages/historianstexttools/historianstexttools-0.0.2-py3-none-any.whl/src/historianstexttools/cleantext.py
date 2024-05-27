import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
import dataloaders


def clean_text(documents, remove_punctuation=True, lowercase=True, removestopwords=True, stopwordslanguage='english',
               removefrequentwords=False, frequentwords=[], lemmatize=True, lemmatizelanguage='english') -> str:

    if remove_punctuation == True:
        documents = remove_punct(documents)

    if lowercase == True:
        documents = apply_lowercase(documents)

    if removestopwords == True:
        documents = remove_stopwords(documents, stopwordslanguage)

    if removefrequentwords == True:
        documents = remove_frequent_words(documents, frequentwords)

    if lemmatize == True:
        documents = lemmatize_text(documents, lemmatizelanguage)

    return documents

def remove_punct(documents) -> str:

    docs = []

    for doc in documents:
        docs.append(re.sub(r'[^\w\s]', '', doc))

    return docs


def apply_lowercase(documents) -> str:

    docs = []

    for doc in documents:
        docs.append(doc.lower())

    return docs


def remove_stopwords(documents, language='english') -> str:

    docs_without_stopwords = []

    nltk.download('stopwords')
    stop_words = set(stopwords.words(language))

    for doc in documents:
        word_tokens = word_tokenize(doc)
        filtered_data = [word for word in word_tokens if not word.lower() in stop_words]
        docs_without_stopwords.append(" ".join(filtered_data))

    return docs_without_stopwords


def remove_frequent_words(documents, frequentwords) -> str:

    docs_without_frequentwords = []

    for doc in documents:
        word_tokens = word_tokenize(doc)
        filtered_data = [word for word in word_tokens if not word.lower() in frequentwords]
        docs_without_frequentwords.append(" ".join(filtered_data))

    return docs_without_frequentwords

def lemmatize_text(documents, language='english') -> str:

    import spacy
    nlp = spacy.load(dataloaders.spacy_models[language])

    lemmatized_docs = []

    for doc in documents:

        current_doc = nlp(doc)
        lemmatized_doc = " ".join([token.lemma_ for token in current_doc])
        lemmatized_docs.append(lemmatized_doc)

    return lemmatized_docs


def part_of_speech_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

