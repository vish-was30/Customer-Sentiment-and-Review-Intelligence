import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def plot_sentiment_distribution(df):
    sns.countplot(x="sentiment", data=df)
    plt.title("Sentiment Distribution")
    plt.savefig("images/sentiment_distribution.jpg")
    plt.show()


def generate_wordcloud(df):
    text = " ".join(df["cleaned_review"])
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title("Word Cloud of Reviews")
    plt.savefig("images/wordcloud.jpg")
    plt.show()