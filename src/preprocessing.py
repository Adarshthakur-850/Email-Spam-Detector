import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import string

def download_nltk_resources():
    nltk.download('stopwords')
    nltk.download('wordnet')

def clean_text(text):
    if not isinstance(text, str):
        return ""
        
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    
    words = text.split()
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return " ".join(words)

def preprocess_data(df):
    download_nltk_resources()
    print("Preprocessing data...")
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    # Ensure text is string
    df['text'] = df['text'].astype(str)
    
    df['cleaned_text'] = df['text'].apply(clean_text)
    return df
