from src.data_loader import load_data
from src.data_loader import load_data
from src.insights import generate_insights
from src.preprocessing import clean_text
from src.sentiment import get_sentiment
from src.model import train_model, predict_review
from src.visualization import plot_sentiment_distribution, generate_wordcloud

# Load dataset
df = load_data("data/reviews.csv")
df = df.dropna(subset=["Text"])

# Pick correct column (UPDATE THIS based on your dataset)
text_column = "Text"

# Apply cleaning
df["cleaned_review"] = df[text_column].apply(clean_text)

# Add and apply sentiment based on scores (UPDATE THIS based on your dataset)
df["sentiment"] = df["Score"].apply(get_sentiment)

# View results
print(df[["cleaned_review", "Score", "sentiment"]].head())
print(df["sentiment"].value_counts(normalize=True))
plot_sentiment_distribution(df)
generate_wordcloud(df)
generate_insights(df)

# Train ML model
model, vectorizer = train_model(df)

# Test with a sample review
sample = "This product is absolutely amazing and tasty"
prediction = predict_review(sample, model, vectorizer)

print("\nSample Prediction:", prediction)