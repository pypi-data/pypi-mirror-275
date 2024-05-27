import cleantext

class HistoriansTextTools:

    def __init__(self, documents=['This is a sample document pushing through the pipeline.'], language='english'):
        self.documents = documents
        self.frequent_words = []
        self.stopwords_language = language
        self.documents_cleaned = cleantext.clean_text(documents)
        self.documents_without_punctuation = cleantext.remove_punct(self.documents)
        self.documents_lowercased = cleantext.apply_lowercase(self.documents)
        self.documents_without_stopwords = cleantext.remove_stopwords(self.documents, self.stopwords_language)
        self.documents_without_frequent_words = cleantext.remove_frequent_words(self.documents, self.frequent_words)
        self.documents_lemmatized = cleantext.lemmatize_text(documents, language)
