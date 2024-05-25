
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

class TextCleaner:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def remove_stopwords(self, text):
        return " ".join([word for word in text.split() if word.lower() not in self.stopwords])

    def to_lowercase(self, text):
        return text.lower()

    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def lemmatize(self, text):
        return " ".join([self.lemmatizer.lemmatize(word) for word in text.split()])
