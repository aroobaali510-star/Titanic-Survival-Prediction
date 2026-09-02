import streamlit as st
import pickle
import pandas as pd

# Page config — must be the first Streamlit command
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    div.stButton > button {
        width: 100%;
        background-color: #0f4c81;
        color: white;
        font-size: 18px;
        font-weight: 600;
        padding: 10px;
        border-radius: 8px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #0a3559;
        color: white;
    }
    h1 {
        color: #0f4c81;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
with open("titanic_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details below to predict survival chances.")
st.divider()

# Layout inputs in two columns instead of one long list
col1, col2 = st.columns(2)

with col1:
    Pclass = st.selectbox("Passenger Class", [1, 2, 3])
    Age = st.number_input(
    "Age",
    min_value=0.0,
    max_value=100.0,
    value=25.0,
    step=1.0
)
    SibSp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
    Fare = st.number_input("Fare", min_value=0.0, value=30.0, step=1.0)

with col2:
    Sex = st.selectbox("Sex", ["male", "female"])
    Embarked = st.selectbox("Embarked Port", ["S", "C", "Q"])
    Parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)

st.divider()

if st.button("🔍 Predict Survival"):

    input_data = pd.DataFrame({
        "Pclass": [Pclass],
        "Sex": [Sex],
        "Age": [Age],
        "SibSp": [SibSp],
        "Parch": [Parch],
        "Fare": [Fare],
        "Embarked": [Embarked]
    })

    prediction = model.predict(input_data)

    st.divider()
    if prediction[0] == 1:
        st.success("This passenger is predicted to SURVIVE!")
        st.balloons()
    else:
        st.error(" This passenger is predicted NOT to survive.")