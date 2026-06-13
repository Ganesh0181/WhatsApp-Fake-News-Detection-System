import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from joblib import dump

# =====================================
# PATH SETUP (IMPORTANT FIX)
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "news.csv")

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv(DATA_PATH)

# Remove missing values
df = df.dropna()

# Ensure correct columns exist
if "text" not in df.columns or "label" not in df.columns:
    raise ValueError("Dataset must contain 'text' and 'label' columns")

X = df["text"]
y = df["label"]

# =====================================
# TRAIN / TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =====================================
# TF-IDF VECTORIZER (IMPROVED)
# =====================================

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7,
    min_df=3,
    ngram_range=(1, 2)
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# =====================================
# MODEL (LOGISTIC REGRESSION)
# =====================================

model = LogisticRegression(
    max_iter=2000,
    solver="liblinear"
)

model.fit(X_train_vec, y_train)

# =====================================
# EVALUATION
# =====================================

predictions = model.predict(X_test_vec)
score = accuracy_score(y_test, predictions)

print("\n========================")
print("MODEL PERFORMANCE")
print("========================")
print("Accuracy:", round(score * 100, 2), "%")
print("========================\n")

# =====================================
# SAVE MODEL (INSIDE SAME FOLDER)
# =====================================

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

dump(model, MODEL_PATH)
dump(vectorizer, VECTORIZER_PATH)

print("Model saved successfully in ml_model/")