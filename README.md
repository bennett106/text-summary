# Text Summarization Application using spaCy and Flask
This is a simple web application that uses the spaCy library for Natural Language Processing (NLP) to summarize text. Given a piece of text, it generates a concise summary of the content. This project is built with Python and the Flask framework.

# Prerequisites
Before running the application, make sure you have the following dependencies installed:
Python 3.x (https://www.python.org/)
Flask (https://flask.palletsprojects.com/)
spaCy (https://spacy.io/)

You can install spaCy and download the English language model by running:

"pip install spacy"

"python -m spacy download en_core_web_sm"

# Getting Started
1. Clone the repository to your local machine:

"git clone https://github.com/yourusername/text-summarization-app.git"

"cd text-summarization-app"

2. Install the required packages:

"pip install -r requirements.txt"

3. Run the Flask Application: 

The application should now be running locally. You can access it in your web browser at http://localhost:5000.

#  Usage
1. Enter or paste the text you want to summarize into the input field.
2. Click the "Summarize" button.
3. The application will process the text using the spaCy model and display the summarized text on the page.

# About spaCy Model
This application uses the spaCy library, a popular NLP library in Python, and the "en_core_web_sm" model for English language processing.
The spaCy model is capable of tokenization, part-of-speech tagging, entity recognition, and sentence parsing, which makes it suitable for 
text summarization tasks.

# Acknowledgments
spaCy: https://spacy.io/
Flask: https://flask.palletsprojects.com/
