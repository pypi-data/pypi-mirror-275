import pandas as pd

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import re
import nltk

nltk.download('stopwords')
nltk.download('wordnet')


class TextCleaner:
    def __init__(self, language='english'):
        try:
            self.stop_words = set(stopwords.words(language))
        except OSError:
            raise ValueError(f"Language '{language}' not supported by NLTK stopwords")
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def to_lowercase(self, text):
        return text.lower()

    def remove_punctuation(self, text):
        return re.sub(r'[^\w\s]', '', text)

    def remove_stopwords(self, text):
        words = text.split()
        filtered_words = [word for word in words if word not in self.stop_words]
        return ' '.join(filtered_words)

    def lemmatize(self, text):
        words = text.split()
        lemmatized_words = [self.lemmatizer.lemmatize(word) for word in words]
        return ' '.join(lemmatized_words)

    def stem(self, text):
        words = text.split()
        stemmed_words = [self.stemmer.stem(word) for word in words]
        return ' '.join(stemmed_words)

    def clean_text(self, text):
        text = self.to_lowercase(text)
        text = self.remove_punctuation(text)
        text = self.remove_stopwords(text)
        text = self.lemmatize(text)
        return text

    def clean_summary(self, text):
        if isinstance(text, str):
            return self.clean_text(text)
        return text

    def clean_all_str(self, df):
        string_columns = df.select_dtypes(include=['object']).columns
        for col in string_columns:
            df[col] = df[col].apply(self.clean_text)

        return df

    def clean_specific_column(self, df, column_name):
        df[column_name] = df[column_name].apply(self.clean_summary)
        return df
