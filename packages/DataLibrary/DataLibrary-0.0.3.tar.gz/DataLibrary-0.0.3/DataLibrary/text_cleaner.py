import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class TextCleaner:
    def _init_(self):
        self.lemmatizer = WordNetLemmatizer()

    def remove_stopwords(self, text):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
        return ' '.join(filtered_text)

    def lowercase(self, text):
        return text.lower()

    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def lemmatize(self, text):
        return ' '.join([self.lemmatizer.lemmatize(word) for word in word_tokenize(text)])