📈 Advertising Sales Prediction Web App

A Machine Learning-powered web application that predicts sales based on advertising budgets using Linear Regression, deployed using Flask.

🔗 Live Demo

https://sales-prediction-yxwf.onrender.com

🧠 Project Overview

This project predicts product sales based on the advertising budget for:

TV

Radio

Newspaper

The Linear Regression model is trained in Python using scikit-learn and integrated into a Flask web app with a responsive UI built using Bootstrap.

🛠 Tech Stack

Python 3.13

Flask

NumPy

Pandas

Scikit-learn

Bootstrap 5

Render (cloud deployment)

📂 Project Structure
sales_prediction/

app.py                  # Flask application
advertisingmodel.pkl    # Trained ML model
requirements.txt        # Python dependencies
Procfile                # For Render deployment
train_model.ipynb       # Jupyter notebook with model training

templates/
   index.html
    result.html

 README.md

🧪 Model Training (Jupyter Notebook)

http://localhost:8888/lab/tree/SalesPrediction.ipynb


⚙️ Local Installation

Run the Flask app:

python app.py


Open your browser at:

http://127.0.0.1:5000/

🌍 Deployment

The app is deployed using Render:

Build Command: pip install -r requirements.txt



🎯 Features

Predicts sales from advertising budget

Clean, responsive UI using Bootstrap

Handles user input validation

Production-ready Flask app

Deployed live on Render

📸 Screenshots

<img width="1918" height="908" alt="image" src="https://github.com/user-attachments/assets/45c3d4a3-b9d2-4473-b705-0d8449e53e76" />

<img width="1916" height="905" alt="image" src="https://github.com/user-attachments/assets/c9bb4203-6683-4dc0-8c14-713534be5c07" />



👩‍💻 Author

Komal Belge
Aspiring ML & Full Stack Developer

⭐ Future Improvements

Add charts to visualize prediction

Improve model accuracy

Add REST API

Deploy with Docker

Add authentication
