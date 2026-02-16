import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'src'))

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.eda import perform_eda
from src.feature_engineering import extract_features
from src.model_trainer import train_models
from src.evaluation import evaluate_models
from src.visualization import plot_model_comparison

def main():
    print("Starting Email Spam Detection Pipeline...")
    
    df = load_data()
    df = preprocess_data(df)
    
    perform_eda(df)
    
    X, y, tfidf = extract_features(df)
    
    results, X_test, y_test = train_models(X, y)
    
    metrics_df = evaluate_models(results, X_test, y_test)
    print("\nModel Comparison:")
    print(metrics_df)
    
    plot_model_comparison(metrics_df)
    
    print("Pipeline completed.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Pipeline Failed: {e}")
