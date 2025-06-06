from flask import Flask, render_template, request
import pandas as pd
import joblib
import re
import os

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(model_path)

# Preprocessing function
def wordpre(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower().strip()
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            txt = request.form['txt']
            txt = wordpre(txt)
            input_data = pd.Series([txt])
            prediction = model.predict(input_data)[0]
            result = 'FAKE' if prediction == 0 else 'REAL'
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
