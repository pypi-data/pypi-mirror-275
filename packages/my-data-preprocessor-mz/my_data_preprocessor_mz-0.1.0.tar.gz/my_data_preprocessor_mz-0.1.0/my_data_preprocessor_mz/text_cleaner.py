import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class TextCleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def remove_stopwords(self, text):
        word_tokens = word_tokenize(text)
        filtered_text = [word for word in word_tokens if word.lower() not in self.stop_words]
        return ' '.join(filtered_text)

    def to_lowercase(self, text):
        return text.lower()

    def remove_punctuation(self, text):
        return re.sub(f"[{re.escape(string.punctuation)}]", "", text)

    def lemmatize_text(self, text):
        word_tokens = word_tokenize(text)
        lemmatized_text = [self.lemmatizer.lemmatize(word) for word in word_tokens]
        return ' '.join(lemmatized_text)

    def clean_text(self, text):
        text = self.to_lowercase(text)
        text = self.remove_punctuation(text)
        text = self.remove_stopwords(text)
        text = self.lemmatize_text(text)
        return text
