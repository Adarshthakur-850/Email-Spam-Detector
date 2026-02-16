from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import joblib
import os
import pandas as pd

def train_models(X, y):
    print("Training models...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"X_train shape: {X_train.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"X_train types: {X_train.dtypes.unique()}")
    print(f"y_train types: {y_train.dtypes}")
    
    # Feature names are lost when converting to numpy array...
    
    models = {
        'NaiveBayes': MultinomialNB(),
        'LogisticRegression': LogisticRegression(max_iter=1000),
        'SVM': LinearSVC(random_state=42, dual=False) # dual=False preferred for n_samples > n_features
    }
    
    if not os.path.exists("models"):
        os.makedirs("models")
        
    best_acc = 0
    best_model = None
    best_name = ""
    
    results = {}
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"{name} Accuracy: {acc:.4f}")
        
        if acc > best_acc:
            best_acc = acc
            best_model = model
            best_name = name
            
        results[name] = model
        
    print(f"Best Model: {best_name} with Accuracy: {best_acc:.4f}")
    joblib.dump(best_model, f"models/best_model_{best_name}.pkl")
    
    return results, X_test, y_test
