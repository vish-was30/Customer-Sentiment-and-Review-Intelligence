from collections import Counter

def get_top_words(text_series, n=10):
    words = " ".join(text_series).split()
    common_words = Counter(words).most_common(n)
    return common_words


def generate_insights(df):
    positive_reviews = df[df["sentiment"] == "Positive"]["cleaned_review"]
    negative_reviews = df[df["sentiment"] == "Negative"]["cleaned_review"]
    neutral_reviews = df[df["sentiment"] == "Neutral"]["cleaned_review"]

    top_positive = get_top_words(positive_reviews)
    top_negative = get_top_words(negative_reviews)
    top_neutral = get_top_words(neutral_reviews)

    print("\nTop words in Positive Reviews:")
    print(top_positive)

    print("\nTop words in Negative Reviews:")
    print(top_negative)

    print("\nTop words in Neutral Reviews:")
    print(top_neutral)