from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def evaluate_models(models, X_test, y_test):
    print("Evaluating models...")
    if not os.path.exists("plots"):
        os.makedirs("plots")
        
    metrics_list = []
    
    for name, model in models.items():
        print(f"Evaluating {name}...")
        y_pred = model.predict(X_test)
        
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        metrics_list.append({
            'Model': name,
            'Accuracy': acc,
            'Precision': report['weighted avg']['precision'],
            'Recall': report['weighted avg']['recall'],
            'F1-Score': report['weighted avg']['f1-score']
        })
        
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f'{name} Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.savefig(f"plots/confusion_matrix_{name}.png")
        plt.close()
        
    metrics_df = pd.DataFrame(metrics_list)
    return metrics_df
