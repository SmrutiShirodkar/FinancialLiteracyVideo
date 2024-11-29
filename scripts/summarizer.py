from transformers import pipeline

def summarize_article(article):
    """
    Summarizes the input article using a pre-trained HuggingFace model.
    """
    summarizer = pipeline("summarization")
    summary = summarizer(article, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    return summary
