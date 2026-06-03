import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from xgboost import XGBClassifier

# Load data
df = pd.read_excel("data/Roopyya_Dataset_10000.xlsx")

# Features
features = [
    "age_years",
    "crif_score",
    "months_in_current_job",
    "net_monthly_salary_inr",
    "requested_amount_inr",
    "requested_tenure_days",
    "true_foir_pct",
    "fraud_flag",
    "wilful_default_flag",
    "pincode_is_serviceable"
]

X = df[features].copy()

# Convert booleans
X["fraud_flag"] = X["fraud_flag"].astype(int)
X["wilful_default_flag"] = X["wilful_default_flag"].astype(int)
X["pincode_is_serviceable"] = X["pincode_is_serviceable"].astype(int)

# Target
y = df["loan_status"]

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    random_state=42
)

model.fit(X_train, y_train)

preds = model.predict(X_test)

print(classification_report(y_test, preds))

joblib.dump(model, "models/model.pkl")
joblib.dump(le, "models/label_encoder.pkl")

print("Model Saved Successfully")