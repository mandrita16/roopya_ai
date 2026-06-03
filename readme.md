# 🏦 Roopya AI — Credit Decision Engine

An AI-powered **credit underwriting and risk assessment system** that evaluates loan applications using machine learning, behavioral scoring, and explainable AI techniques.

It simulates real-world banking decision systems used in fintech and lending institutions.

---

## 🚀 Live Demo

https://roopya-ai.streamlit.app/

---

##  Project Overview

Roopya AI automates loan eligibility decisions using:
- Credit scoring model (ML-based)
- Financial behavior analysis
- Risk estimation engine
- Applicant similarity (Twin system)
- Recommendation + reason generation

It not only predicts approval but also explains **why a decision was made**.

---

##  Key Features

### 🔹 1. Credit Decision Engine
- Predicts: **Approved / Rejected**
- Based on:
  - CRIF Score
  - Salary
  - FOIR (Debt burden)
  - Employment stability
  - Fraud indicators

---

### 🔹 2. Risk Scoring System
- Computes custom **Risk DNA Score**
- Combines financial + behavioral features

---

### 🔹 3. Applicant Twin Analysis
- Finds similar historical applicants
- Shows approval probability based on peer group

---

### 🔹 4. Loan Recommendation Engine
- Suggests optimized loan amount
- Reduces default risk exposure

---

### 🔹 5. Explainable AI Layer (Rule-based)
- Generates human-readable reasons:
  - High FOIR impact
  - Low credit score impact
  - Fraud risk detection

---

### 🔹 6. 3D Approval Trajectory
- Visualizes how approval probability changes with:
  - CRIF Score
  - FOIR
  - Salary

---

##  System Architecture

<img width="1309" height="1314" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/912901c6-e85c-47c9-a5d6-4c0d5e395791" />

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend Logic:** Python
- **ML Framework:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly
- **Model Storage:** Joblib
(written in detail below)

---
##  Machine Learning & Data Processing Stack

###  Core ML Frameworks
- scikit-learn==1.9.0 → Model training, preprocessing, classification
- xgboost==3.2.0 → Gradient boosting models for improved accuracy
- scipy==1.17.1 → Scientific computations and statistical operations
- numba==0.65.1 → Performance optimization for numerical operations
- llvmlite==0.47.0 → JIT compilation backend for numba

---

### 📊 Data Processing & Analysis
- pandas==3.0.3 → Data manipulation and feature engineering
- numpy==2.4.6 → Numerical computations and array processing
- openpyxl==3.1.5 → Excel dataset handling (.xlsx files)
- pyarrow==24.0.0 → Efficient data serialization and processing

---

### 📈 Data Visualization
- plotly==6.7.0 → Interactive charts, risk gauges, 3D trajectory plots
- shap==0.52.0 → Model explainability and feature importance analysis

---

### 🧾 Data Validation & Schema Handling
- jsonschema==4.26.0 → Input validation and structured data checking
- attrs==26.1.0 → Clean data structure definitions

---

### ⚙️ Model Utilities & Persistence
- joblib==1.5.3 → Model saving and loading
- cloudpickle==3.1.2 → Serialization of ML objects

---

### 🔄 Supporting Libraries
- python-dateutil==2.9.0.post0 → Date handling for time-based features
- tqdm==4.67.3 → Progress tracking during training
- threadpoolctl==3.6.0 → Parallel processing control
  
---


## 📂 Project Structure
```
roopya_ai/
│
├── frontend/
│   ├── app.py                  # Streamlit UI (main entry point)
│   └── __init__.py
│
├── utils/
│   ├── credit_metrics.py      # Risk + credit health calculations
│   ├── reason_engine.py       # Explanation generator
│   ├── recommendation_engine.py # Loan optimization logic
│   ├── applicant_twin.py      # Similar applicant analysis
│   ├── similarity.py          # Similarity computation logic
│   ├── predict.py            # Model inference wrapper
│   ├── explain.py            # (future SHAP integration)
│   ├── check_columns.py     # Input validation
│   └── train_model.py       # Model training pipeline
│
├── models/
│   ├── model.pkl             # Trained ML model
│   └── label_encoder.pkl     # Output encoding
│
├── data/
│   └── Roopyya_Dataset_10000.xlsx
│
├── notebooks/ (optional)
│   └── model_training.ipynb
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```
---
## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/mandrita16/roopya_ai.git
cd roopya_ai
```
### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
```
Activate it:
Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Application
```bash
streamlit run frontend/app.py
```
### 5. Deactivate Environment (Optional)
```bash
deactivate
```
---

## 📈 ML Pipeline

1. Data Preprocessing
2. Feature Engineering
3. Model Training (Classification)
4. Encoding Labels
5. Probability Estimation
6. Decision Thresholding

---

## 📊 Sample Input Features

- Age
- CRIF Score
- Monthly Income
- Job Stability (months)
- Loan Amount
- FOIR %
- Fraud Flag
- Wilful Default Flag

---

##  Output

- Loan Decision: **Approved / Rejected**
- Confidence Score (%)
- Risk Score (0–100)
- Loan Recommendation
- Reason Explanation
- Approval Trajectory Visualization

---

##  Future Enhancements

- SHAP Explainability Integration
- What-If Scenario Simulator
- Deep Learning Credit Risk Model
- API-based deployment (FastAPI)
- Real-time credit scoring engine

---

## 📌 Use Case

This project simulates real-world systems used in:
- Banks 
- NBFCs
- Fintech startups
- Credit underwriting platforms

---
##  Project Highlights

- Real-time loan approval prediction system
- Explainable AI decision engine
- Risk scoring system (custom-built)
- Applicant similarity (Twin model)
- Interactive 3D approval trajectory visualization
- 
---
## 👩‍💻 Author

**Mandrita Dasgupta**   

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and connect!
