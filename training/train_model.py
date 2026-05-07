import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nlp.preprocess import TextPreprocessor
from ip.ip_features import IPFeatureExtractor

def train():
    print("Loading data...")
    try:
        df = pd.read_csv('data/news.csv')
    except FileNotFoundError:
        print("Error: data/news.csv not found. Please ensure data generation step completed.")
        return

    X = df[['text', 'ip_address']]
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Building pipeline...")
    
    # NLP Pipeline
    text_pipeline = Pipeline([
        ('preprocessor', TextPreprocessor()),
        ('tfidf', TfidfVectorizer(max_features=5000))
    ])

    # IP Pipeline
    # Note: IPFeatureExtractor returns a list of dicts, DictVectorizer converts to matrix
    ip_pipeline = Pipeline([
        ('extractor', IPFeatureExtractor()),
        ('vectorizer', DictVectorizer(sparse=False))
    ])

    # Combined Features
    preprocessor = ColumnTransformer(
        transformers=[
            ('text', text_pipeline, 'text'),
            ('ip', ip_pipeline, 'ip_address')
        ]
    )

    # Full Pipeline
    model_pipeline = Pipeline([
        ('features', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    print("Training model (this may take time due to IP lookups)...")
    # Warning: IP lookups in loop are slow. For production, offline processing is better.
    # For this demo, it's acceptable but will be slow if dataset is large.
    model_pipeline.fit(X_train, y_train)

    print("Evaluating model...")
    y_pred = model_pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))

    print("Saving model...")
    os.makedirs('models', exist_ok=True)
    joblib.dump(model_pipeline, 'models/model.pkl')
    print("Model saved to models/model.pkl")

if __name__ == "__main__":
    train()
