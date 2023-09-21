import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarizer(rawdocs):

    stopwords = list(STOP_WORDS)
    # print(stopwords)

    punc = list(punctuation)
    # print(punc)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    # print(doc)

    tokens = [token.text for token in doc]
    # print(tokens)


    #to get the frequency of the repeated words.
    word_frequency = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_frequency.keys():
                word_frequency[word.text] = 1
            else:
                word_frequency[word.text] += 1

    # print(word_frequency)

    max_frequency = max(word_frequency.values())
    # print(max_frequency)

    for word in word_frequency.keys():
        word_frequency[word] = word_frequency[word]/max_frequency
    # print(word_frequency)
    #normalised frequency

    sentence_tokens = [sentence for sentence in doc.sents]
    # print(sentence_tokens)

    #to get the frequency of the sentences repeated
    sentence_scores = {}
    for sentence in sentence_tokens:
        for word in sentence:
            if word.text in word_frequency.keys():
                if sentence not in sentence_scores.keys():
                    sentence_scores[sentence] = word_frequency[word.text]
                else:
                    sentence_scores[sentence] += word_frequency[word.text]

    # print(sentence_scores)

    select_len = int(len(sentence_tokens) * 0.3)
    # print(select_len)

    summary = nlargest(select_len, sentence_scores, key = sentence_scores.get)
    # print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # # print(summary)         remove the comment 

    # print("Length of original text",len(text.split(' ')))
    # print("Length of summary text",len(summary.split(' ')))

    len_orig_txt = len(rawdocs.split(' '))
    len_summary = len(summary.split(' '))
    original_txt = doc

    return summary, original_txt, len_orig_txt, len_summary



















# Text mining, also known as text data mining or text analytics, is the process of extracting valuable information and insights from large volumes of unstructured textual data. It involves using various natural language processing (NLP) and machine learning techniques to analyze, understand, and interpret the content of text documents. Text mining aims to discover patterns, trends, relationships, and knowledge hidden within the text, enabling businesses and researchers to make data-driven decisions and gain a deeper understanding of the data they possess.Text mining finds applications in various domains, such as market research, customer feedback analysis, social media monitoring, healthcare and biomedicine, fraud detection, legal discovery, and more. It enables businesses and organizations to harness the vast amount of unstructured text data available today to make informed decisions, understand customer sentiments, and discover valuable information that may have otherwise remained hidden.