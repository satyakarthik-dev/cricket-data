# 🏏 Cricket Runs Prediction App

---

## 🚀 Features

* 📊 Predict runs using:

  * Balls Faced
  * Number of Fours
  * Number of Sixes
  * Strike Rate
* ⚡ Real-time prediction using Streamlit UI
* 🤖 Machine Learning model (Linear Regression)
* 📁 Simple and beginner-friendly project structure

---

## 🧠 Machine Learning Model

* Algorithm Used: **Linear Regression**
* Input Features:

  * `Balls_Faced`
  * `Fours`
  * `Sixes`
  * `Strike_Rate`
* Output:

  * `Runs`

---

## 🖥️ User Interface

The app is built using **Streamlit**, where users can:

* Enter player statistics
* Click on **Predict Runs**
* Instantly get predicted results

---

## 📁 Project Structure

```
cricket-app/
│
├── app.py
├── cricket_dataset.csv
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cricket-app.git
cd cricket-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deployment

You can deploy this app easily using **Streamlit Cloud**:

1. Push your code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your repository
4. Deploy 🚀

---

## 📊 Example Input

| Balls Faced | Fours | Sixes | Strike Rate |
| ----------- | ----- | ----- | ----------- |
| 45          | 5     | 2     | 120.5       |

👉 Output: Predicted Runs

---

## 🔧 Technologies Used

* Python 🐍
* Pandas
* Scikit-learn
* Streamlit

---

## ❗ Common Error

**FileNotFoundError: cricket_dataset.csv**

👉 Solution:

* Make sure the dataset file is in the same folder as `app.py`

---

## 📌 Future Improvements

* Add multiple ML models (Random Forest, Decision Tree)
* Improve UI with charts 📊
* Deploy as a live public app 🌐
* Add player name and match details

---

## 🙌 Author

**Karthik**
Final Year Engineering Student (ECE)

---

## ⭐ Support

If you like this project:

* Give it a ⭐ on GitHub
* Share with your friends

---
