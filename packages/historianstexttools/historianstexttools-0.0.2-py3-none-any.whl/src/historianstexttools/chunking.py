def sentence_chunking(documents, language='english'):
    from nltk.tokenize import sent_tokenize

    sentences = []

    for doc in documents:
        doc_sentences = sent_tokenize(doc, language=language)
        for sentence in doc_sentences:
            sentences.append(sentence)

    return sentences

def wordcount_chunking(documents, chunk_size, overlap=0):
    chunked_documents = []

    for doc in documents:
        split_doc = doc.split()
        doc_length = len(split_doc)

        if doc_length > chunk_size:
            beginning = 0

            while beginning < doc_length:
                beginning = max(beginning - overlap, 0)
                print(beginning)
                end = min(beginning + chunk_size, doc_length)
                current_chunk_array = split_doc[beginning:end]
                chunked_documents.append(' '.join(current_chunk_array))
                beginning = end

        else:
            chunked_documents.append(doc)

    return chunked_documents