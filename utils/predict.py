import pandas as pd
import joblib
from reason_engine import generate_reasons
reasons = generate_reasons(
    crif=780,
    foir=25,
    fraud=False,
    wilful_default=False,
    serviceable=True
)

print("\nReasons:")

for r in reasons:
    print("-", r)
model = joblib.load("models/model.pkl")
encoder = joblib.load("models/label_encoder.pkl")

sample = pd.DataFrame([{
    "age_years":29,
    "crif_score":780,
    "months_in_current_job":24,
    "net_monthly_salary_inr":70000,
    "requested_amount_inr":150000,
    "requested_tenure_days":365,
    "true_foir_pct":25,
    "fraud_flag":0,
    "wilful_default_flag":0,
    "pincode_is_serviceable":1
}])

prediction = model.predict(sample)

result = encoder.inverse_transform(prediction)

print("Decision:", result[0])

proba = model.predict_proba(sample)

print("Confidence:", round(proba.max()*100,2), "%")