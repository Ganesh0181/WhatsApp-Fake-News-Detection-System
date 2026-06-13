import joblib
import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "ml-model",
    "model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "..",
    "ml-model",
    "vectorizer.pkl"
)

model = joblib.load(MODEL_PATH)

vectorizer = joblib.load(VECTORIZER_PATH)

def predict_news(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    decision_score = model.decision_function(
        text_vector
    )

    confidence = round(
        min(abs(decision_score[0]) * 75, 99),
        2
    )

    if confidence < 50:
        confidence += 30

    return prediction, confidence