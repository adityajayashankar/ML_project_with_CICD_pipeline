#  Student Performance Prediction – End-to-End ML Pipeline with CI/CD

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8-blue" alt="Python Version">
  </a>
  <a href="https://github.com/adityajayashankar/ML-project/actions/workflows/main.yml">
    <img src="https://github.com/adityajayashankar/ML-project/actions/workflows/main.yml/badge.svg" alt="CI/CD Status">
  </a>
  <a href="https://ml-project-with-deployment-z5u7.onrender.com">
    <img src="https://img.shields.io/badge/Deployed%20on-Render-success" alt="Render Deployment">
  </a>
  <a href="https://choosealicense.com/licenses/mit/">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
  </a>
</p>


## 🚀 Live Demo

 [Click here to open the app](https://ml-project-with-deployment-z5u7.onrender.com)

---

## Project Overview

This project is an end-to-end machine learning pipeline designed to predict student performance based on demographic and academic features. It includes:

-  Data ingestion, preprocessing, model training
-  Flask web app with prediction form
-  Docker containerization
-  Deployment on **Render** with **CI/CD** via GitHub Actions

---

## Tech Stack

- Python 3.8
- Scikit-learn
- Pandas, NumPy
- Flask
- Docker
- Render
- GitHub Actions

---

## Project Structure

├── app.py # Flask application <br>
├── Dockerfile # Docker config <br>
├── requirements.txt # Project dependencies <br>
├── templates/ <br>
│ ├── home.html # Prediction form <br>
│ └── index.html # Landing page <br>
├── artifacts/ # Stores models, preprocessor, datasets <br>
├── src/ <br>
│ ├── components/ # Data ingestion, transformation, training <br>
│ ├── pipeline/ <br>
│ │ ├── predict_pipeline.py # Prediction logic <br>
│ │ └── train_pipeline.py # Training logic <br>
│ ├── utils.py # Helper functions <br>
│ ├── logger.py # Logs setup <br>
│ └── exception.py # Custom error handling <br>
├── .github/workflows/ <br>
│ └── main.yml # GitHub Actions for CI/CD <br>

yaml
Copy
Edit

---

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/adityajayashankar/ML-project.git
cd ML-project

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # (Windows)
# source venv/bin/activate  # (macOS/Linux)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
Open http://127.0.0.1:5000/predictdata in your browser.

Docker Usage
bash
Copy
Edit
docker build -t mlproject-app .
docker run -p 5000:5000 mlproject-app
 CI/CD with GitHub Actions
Every push to main triggers:

 Automated testing

 Build and deployment to Render

Workflow file: .github/workflows/main.yml

 Model Info
Input Features: Gender, Ethnicity, Parental Education, Lunch, Test Prep, Reading & Writing Scores

Output: Predicted Math Score

Models Used: Linear Regression, Random Forest, XGBoost, CatBoost

Best R² Score: ~85%
```
#  Contact
 Email: adityajayashankar@gmail.com

 GitHub: @adityajayashankar

#  License
Licensed under the MIT License.


  


