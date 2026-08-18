import os

import streamlit as st
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression


st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)


st.title("🚢 Titanic Survival Predictor")

st.write(
    "Predict the probability of survival for a Titanic passenger "
    "using a machine learning model."
)


# -----------------------------
# PATH SETUP
# -----------------------------
# Always look for the CSV next to this script, no matter where
# `streamlit run` is called from.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "titanic.csv")


# -----------------------------
# TRAIN MODEL (cached — runs once, not on every click/rerun)
# -----------------------------

@st.cache_resource
def train_model():
    if not os.path.exists(DATA_PATH):
        st.error(
            f"Could not find titanic.csv at:\n{DATA_PATH}\n\n"
            "Make sure titanic.csv is saved in the same folder as app.py."
        )
        st.stop()

    df = pd.read_csv(DATA_PATH)
    df.columns = [c.strip().lower() for c in df.columns]

    # -----------------------------
    # FEATURE ENGINEERING
    # -----------------------------
    df["family_size"] = df["sibsp"] + df["parch"] + 1
    df["is_alone"] = (df["family_size"] == 1).astype(int)
    df["fare_per_person"] = df["fare"] / df["family_size"]

    # -----------------------------
    # FEATURES AND TARGET
    # -----------------------------
    features = [
        "pclass",
        "sex",
        "age",
        "fare",
        "embarked",
        "family_size",
        "is_alone",
        "fare_per_person",
    ]

    X = df[features]
    y = df["survived"]

    numeric_features = [
        "pclass",
        "age",
        "fare",
        "family_size",
        "is_alone",
        "fare_per_person",
    ]

    categorical_features = [
        "sex",
        "embarked",
    ]

    # -----------------------------
    # PREPROCESSING
    # -----------------------------
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ])

    # -----------------------------
    # MODEL
    # -----------------------------
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000)),
    ])

    model.fit(X, y)

    return model


model = train_model()


# -----------------------------
# USER INPUT
# -----------------------------

st.subheader("Enter Passenger Details")

pclass = st.selectbox("Passenger Class", [1, 2, 3])

sex = st.selectbox("Sex", ["male", "female"])

age = st.number_input("Age", min_value=0.0, max_value=100.0, value=25.0)

fare = st.number_input("Fare", min_value=0.0, value=30.0)

embarked = st.selectbox("Embarked", ["S", "C", "Q"])

family_size = st.number_input("Family Size", min_value=1, max_value=20, value=1)

is_alone = 1 if family_size == 1 else 0
fare_per_person = fare / family_size


# -----------------------------
# PREDICTION
# -----------------------------

if st.button("Predict Survival"):

    passenger = pd.DataFrame({
        "pclass": [pclass],
        "sex": [sex],
        "age": [age],
        "fare": [fare],
        "embarked": [embarked],
        "family_size": [family_size],
        "is_alone": [is_alone],
        "fare_per_person": [fare_per_person],
    })

    prediction = model.predict(passenger)[0]
    probability = model.predict_proba(passenger)[0][1]

    st.subheader("Prediction")

    if prediction == 1:
        st.success("🟢 Likely to Survive")
    else:
        st.error("🔴 Likely Not to Survive")

    st.metric("Survival Probability", f"{probability * 100:.2f}%")