import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

def perform_eda(df):
    print("Performing EDA...")
    if not os.path.exists("plots"):
        os.makedirs("plots")
        
    plt.figure(figsize=(6, 4))
    sns.countplot(x='spam', data=df)
    plt.title("Spam vs Ham Distribution")
    plt.savefig("plots/spam_distribution.png")
    plt.close()
    
    spam_text = " ".join(df[df['spam']==1]['cleaned_text'])
    ham_text = " ".join(df[df['spam']==0]['cleaned_text'])
    
    spam_wc = WordCloud(width=800, height=400, background_color='white').generate(spam_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(spam_wc, interpolation='bilinear')
    plt.axis("off")
    plt.title("Spam WordCloud")
    plt.savefig("plots/spam_wordcloud.png")
    plt.close()
    
    ham_wc = WordCloud(width=800, height=400, background_color='white').generate(ham_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(ham_wc, interpolation='bilinear')
    plt.axis("off")
    plt.title("Ham WordCloud")
    plt.savefig("plots/ham_wordcloud.png")
    plt.close()
