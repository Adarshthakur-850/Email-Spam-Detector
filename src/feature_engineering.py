from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def extract_features(df):
    print("Extracting features...")
    df['text_length'] = df['cleaned_text'].apply(len)
    
    # Validating data type
    print(f"Cleaned text nulls: {df['cleaned_text'].isnull().sum()}")
    df['cleaned_text'] = df['cleaned_text'].astype(str)
    
    tfidf = TfidfVectorizer(max_features=3000)
    X_tfidf = tfidf.fit_transform(df['cleaned_text']).toarray()
    
    X_features = pd.DataFrame(X_tfidf)
    X_features['text_length'] = df['text_length'].values
    
    # Ensure column names are strings (sklearn requirement for mixed types)
    X_features.columns = X_features.columns.astype(str)
    
    return X_features, df['spam'], tfidf
