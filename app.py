import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    data = pd.read_csv("cricket_dataset.csv")
    return data

data = load_data()

# -------------------------------
# Train Model
# -------------------------------
@st.cache_resource
def train_model(data):
    X = data[['Balls_Faced', 'Fours', 'Sixes', 'Strike_Rate']]
    y = data['Runs']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

model = train_model(data)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🏏 Cricket Runs Predictor")

st.write("Enter player details to predict runs")

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
# Show Dataset (Optional)
# -------------------------------
if st.checkbox("Show Dataset"):
    st.write(data.head())