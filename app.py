import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -------------------------------
# Dummy Dataset (for training)
# -------------------------------
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'Runs':        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Balls_Faced': [10, 20, 25, 35, 40, 45, 50, 55, 60, 65],
        'Fours':       [1, 2, 3, 4, 5, 6, 6, 7, 8, 9],
        'Sixes':       [0, 1, 1, 2, 2, 3, 3, 4, 4, 5],
        'Strike_Rate': [100, 100, 120, 114, 125, 133, 140, 145, 150, 155]
    })
    return data

data = load_data()

# -------------------------------
# Train Model
# -------------------------------
@st.cache_resource
def train_model(data):
    X = data[['Runs', 'Balls_Faced', 'Fours', 'Sixes']]
    y = data['Strike_Rate']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

model = train_model(data)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🏏 Strike Rate Predictor")

st.write("Enter player stats below:")

# 👉 Empty user inputs (no default values)
runs = st.number_input("Runs", min_value=0, value=None, placeholder="Enter runs scored")
balls = st.number_input("Balls Faced", min_value=1, value=None, placeholder="Enter balls faced")
fours = st.number_input("Fours", min_value=0, value=None, placeholder="Enter number of fours")
sixes = st.number_input("Sixes", min_value=0, value=None, placeholder="Enter number of sixes")

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Strike Rate"):

    if runs is None or balls is None or fours is None or sixes is None:
        st.warning("⚠️ Please enter all input values")
    else:
        input_data = [[runs, balls, fours, sixes]]
        prediction = model.predict(input_data)

        st.success(f"🔥 Predicted Strike Rate: {round(prediction[0], 2)}")

# -------------------------------
# Optional Dataset View
# -------------------------------
if st.checkbox("Show Sample Dataset"):
    st.write(data)
