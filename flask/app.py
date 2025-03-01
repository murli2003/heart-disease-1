from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs
        age = int(request.form['age'])
        cp = int(request.form['cp'])
        thalach = int(request.form['thalach'])
        
        # Create a DataFrame for the input
        user_data = pd.DataFrame({'age': [age], 'cp': [cp], 'thalach': [thalach]})
        
        # Make prediction
        prediction = model.predict(user_data)
        result = "Heart disease present" if prediction[0] == 1 else "Heart disease not present"
        
        return render_template('index.html', prediction=result)
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
