import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class text_cleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
    
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = ' '.join(word for word in text.split() if word not in self.stop_words)
        text = ' '.join(self.lemmatizer.lemmatize(word) for word in text.split())
        return text
    
    def clean_column(self, df, column):
        df[column] = df[column].apply(self.clean_text)
        return df
