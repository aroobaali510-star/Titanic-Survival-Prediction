# 🚢 Titanic Survival Prediction

A Machine Learning web app that predicts whether a Titanic passenger would have survived, based on their details — built with Python, Scikit-learn, and deployed using Streamlit.

## 📌 Project Overview

This project uses the classic Titanic dataset to train a Logistic Regression model that predicts passenger survival. It covers the full ML workflow — data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment as an interactive web app.

## 🔧 Features Used

- Pclass (Passenger Class)
- Sex
- Age
- SibSp (Siblings/Spouses Aboard)
- Parch (Parents/Children Aboard)
- Fare
- Embarked (Port of Embarkation)

## 🛠️ Tech Stack

- **Python**
- **Pandas / NumPy** — data handling
- **Matplotlib / Seaborn** — visualization & EDA
- **Scikit-learn** — preprocessing (SimpleImputer, MinMaxScaler, OneHotEncoder, ColumnTransformer) and model training (Logistic Regression)
- **Streamlit** — web app deployment

## ⚙️ How It Works

1. Raw passenger data is cleaned and preprocessed (missing values handled, categorical features encoded, numerical features scaled)
2. A Logistic Regression model is trained on the processed data
3. Preprocessing and the trained model are combined into a single Scikit-learn Pipeline and saved as `titanic_model.pkl`
4. The Streamlit app (`app.py`) loads this pipeline and predicts survival based on user input

## 🚀 Running the App Locally

```bash
git clone https://github.com/aroobaaliatgit/Titanic-dataset.git
cd Titanic-dataset
pip install streamlit pandas scikit-learn
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## 📂 Project Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit web app for making predictions |
| `titanic_model.pkl` | Trained pipeline (preprocessing + Logistic Regression model) |
| `*.ipynb` | Jupyter notebook with EDA, preprocessing, training, and evaluation |

## 📊 Model

Logistic Regression, evaluated using accuracy score, classification report, and confusion matrix.

## 👤 Author

**Arooba Ali**
# Titanic-Survival-Prediction
Machine learning project predicting Titanic passenger survival using classification models — built with Python, Pandas &amp; Scikit-learn.
