import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import PassiveAggressiveClassifier

from sklearn.metrics import accuracy_score

from joblib import dump

# Load dataset

df = pd.read_csv("news.csv")

X = df["text"]

y = df["label"]

# Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# TF-IDF

vectorizer = TfidfVectorizer(
    stop_words="english"
)

X_train_vector = vectorizer.fit_transform(X_train)

X_test_vector = vectorizer.transform(X_test)

# Model

model = PassiveAggressiveClassifier()

model.fit(
    X_train_vector,
    y_train
)

# Accuracy

predictions = model.predict(X_test_vector)

score = accuracy_score(
    y_test,
    predictions
)

print("Accuracy:", score * 100)

# Save

dump(model, "model.pkl")

dump(vectorizer, "vectorizer.pkl")

print("Model Saved")