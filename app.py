import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -------------------------------
# Create Dummy Dataset (NO CSV)
# -------------------------------
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'Balls_Faced': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        'Fours':       [0, 1, 2, 2, 3, 4, 4, 5, 5, 6],
        'Sixes':       [0, 0, 1, 1, 1, 2, 2, 2, 3, 3],
        'Strike_Rate': [80, 90, 100, 110, 120, 130, 135, 140, 145, 150],
        'Runs':        [4, 12, 20, 28, 35, 45, 55, 65, 75, 90]
    })
    return data

data = load_data()

# -------------------------------
# Train Model
# -------------------------------
@st.cache_resource
def train_model(data):
    X = data[['Balls_Faced', 'Fours', 'Sixes', 'Strike_Rate']]
    y = data['Runs']
    
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
st.title("🏏 Cricket Runs Predictor (No CSV Version)")

st.write("Enter player stats to predict runs")

# User Inputs
balls = st.number_input("Balls Faced", min_value=0)
fours = st.number_input("Fours", min_value=0)
sixes = st.number_input("Sixes", min_value=0)
strike_rate = st.number_input("Strike Rate", min_value=0.0)

# Prediction
if st.button("Predict Runs"):
    input_data = [[balls, fours, sixes, strike_rate]]
    prediction = model.predict(input_data)
    
    st.success(f"🏆 Predicted Runs: {round(prediction[0], 2)}")

# -------------------------------
# Optional: Show Dataset
# -------------------------------
if st.checkbox("Show Sample Dataset"):
    st.write(data)
