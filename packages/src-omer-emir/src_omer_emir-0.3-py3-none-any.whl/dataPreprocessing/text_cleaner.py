import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

class TextCleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def removeStopwords(self, text):
        words = text.split()
        words = [word for word in words if word.lower() not in self.stop_words]
        return ' '.join(words)

    def toLowercase(self, text):
        return text.lower()

    def removePunctuation(self, text):
        return re.sub(r'[^\w\s]', '', text)

    def lemmatize(self, text):
        words = text.split()
        words = [self.lemmatizer.lemmatize(word) for word in words]
        return ' '.join(words)