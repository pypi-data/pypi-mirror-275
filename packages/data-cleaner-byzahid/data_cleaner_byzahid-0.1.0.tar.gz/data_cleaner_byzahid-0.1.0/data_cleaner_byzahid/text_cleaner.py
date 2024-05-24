import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


class TextCleaner:

    def __init__(self, text):
        self.text = text

    def lowercase(self):
        self.text = self.text.lower()
        return self.text

    def remove_punctuation(self):
        self.text = self.text.translate(str.maketrans('', '', string.punctuation))
        return self.text

    def remove_numbers(self):
        self.text = re.sub(r'\d+', '', self.text)
        return self.text

    def remove_stopwords(self, language='english'):
        stop_words = set(stopwords.words(language))
        self.text = ' '.join([word for word in self.text.split() if word not in stop_words])
        return self.text

    def stem_text(self):
        stemmer = PorterStemmer()
        self.text = ' '.join([stemmer.stem(word) for word in self.text.split()])
        return self.text

    def lemmatize_text(self):
        lemmatizer = WordNetLemmatizer()
        self.text = ' '.join([lemmatizer.lemmatize(word) for word in self.text.split()])
        return self.text

    def remove_whitespace(self):
        self.text = ' '.join(self.text.split())
        return self.text

    def remove_special_characters(self):
        self.text = re.sub(r'[^a-zA-Z\s]', '', self.text)
        return self.text