from keybert import KeyBERT

def extract_keywords(text):
    """
    Extracts keywords from the text using KeyBERT.
    """
    kw_model = KeyBERT()
    sentences = text.split('.')
    keywords = [kw_model.extract_keywords(sentence, keyphrase_ngram_range=(2, 2), top_n=1)[0][0] for sentence in sentences if sentence]
    return keywords, sentences
