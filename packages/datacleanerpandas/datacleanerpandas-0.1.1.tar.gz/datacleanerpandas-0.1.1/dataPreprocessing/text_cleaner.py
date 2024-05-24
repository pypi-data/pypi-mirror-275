import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Downloading necessary data sets from NLTK
nltk.download('stopwords')
nltk.download('wordnet')


class TextCleaner:


    def __init__(self, remove_stopwords=True, lemmatize=True):
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize
        self.stopwords = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def clean(self, text):
        # Convert text to lowercase
        text = text.lower()

        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)

        # Split text into words
        words = text.split()

        # Remove short words
        words = [word for word in words if len(word) > 2]

        # Remove stopwords
        if self.remove_stopwords:
            words = [word for word in words if word not in self.stopwords]

        # Lemmatize words
        if self.lemmatize:
            words = [self.lemmatizer.lemmatize(word) for word in words]

        # Return the cleaned words as a joined string
        return ' '.join(words)
