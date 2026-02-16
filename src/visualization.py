import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_model_comparison(metrics_df):
    if not os.path.exists("plots"):
        os.makedirs("plots")
        
    plt.figure(figsize=(10, 6))
    melted_df = metrics_df.melt(id_vars="Model", var_name="Metric", value_name="Score")
    
    sns.barplot(x="Model", y="Score", hue="Metric", data=melted_df)
    plt.title("Model Performance Comparison")
    plt.ylim(0, 1.1)
    plt.legend(loc='lower right')
    plt.savefig("plots/model_comparison.png")
    plt.close()
