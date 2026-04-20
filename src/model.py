from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

def train_model(df):
    X = df["cleaned_review"]
    y = df["sentiment"]

    # Convert text → numbers
    vectorizer = TfidfVectorizer(
    max_features=7000,
    stop_words="english",
    ngram_range=(1,2)
)
    X_vectorized = vectorizer.fit_transform(X)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_vectorized, y, test_size=0.2, random_state=42
    )

    print("\n---Logistic Regression")

    # Train Logistic Regression Model
    lr = LogisticRegression(max_iter=500, class_weight="balanced")
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    print(classification_report(y_test, y_pred_lr))

    print("\n--- Naive Bayes ---")
    # Train Naive Bayes Model
    nb = MultinomialNB()
    nb.fit(X_train, y_train)
    y_pred_nb = nb.predict(X_test)
    print(classification_report(y_test, y_pred_nb))

    return lr, vectorizer
    print("\nModel Performance:\n")
    print(classification_report(y_test, y_pred))

    return model, vectorizer

def predict_review(text, model, vectorizer):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]