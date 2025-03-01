# Heart Disease Prediction using Flask & Machine Learning

## 📌 Project Overview

This project is a **Heart Disease Prediction Web App** built using **Flask** and a **Logistic Regression model** trained on a dataset containing patient details. Users can input their age, chest pain type, and maximum heart rate to get a prediction on whether they might have heart disease.

## 🚀 Features

- Interactive **Flask Web Application**
- Uses a **pre-trained machine learning model (Logistic Regression)**
- Simple and user-friendly UI with a **colorful background**
- **Predict button** to generate results instantly
- Deployable on **Heroku, Render, or AWS**

## 🛠️ Technologies Used

- **Python** (for backend logic)
- **Flask** (for web framework)
- **Joblib** (to load the trained model)
- **Pandas** (for handling data)
- **Scikit-learn** (for machine learning operations)
- **HTML & CSS** (for frontend UI)

## 📂 Project Structure

```
project/
│
├── app.py                 # Main Flask application
├── heart_disease_model.pkl  # Trained ML model (saved using joblib)
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   └── index.html         # Webpage UI
└── static/                # Static files (CSS, images)
```

## 🔧 Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Install Python & Virtual Environment

Make sure **Python 3.x** is installed. Then, create and activate a virtual environment:

```bash
python -m venv venv   # Create virtual environment
venv\Scripts\activate  # Activate on Windows
source venv/bin/activate  # Activate on Mac/Linux
```

### 2️⃣ Install Required Libraries

Run the following command:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install flask joblib pandas scikit-learn
```

### 3️⃣ Run the Flask App

Execute:

```bash
python app.py
```

The app will be available at [**http://127.0.0.1:5000**](http://127.0.0.1:5000).

## 🎨 User Interface

The app has a **colorful background** or an image-based UI. Users enter **age, chest pain type (0-3), and maximum heart rate achieved**, then click the **"Predict"** button to get results.

## 🌍 Deployment

To deploy on **Heroku**:

```bash
pip freeze > requirements.txt   # Create dependencies file
echo "web: python app.py" > Procfile   # Create Heroku Procfile
git init
git add .
git commit -m "Initial commit"
heroku create
heroku git:remote -a <your-heroku-app-name>
git push heroku master
heroku open
```

## 🤖 Model Details

- Model: **Logistic Regression**
- Features Used: `age`, `cp` (chest pain type), `thalach` (maximum heart rate achieved)
- Dataset: Public **heart disease dataset**
---

💡 **Need Help?** Feel free to ask! 🚀

