import sys
import os
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
import numpy as np
import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

from utils.credit_metrics import calculate_credit_health
from utils.recommendation_engine import loan_recommendation
from utils.reason_engine import generate_reasons
from utils.applicant_twin import applicant_twin

from utils.reason_engine import generate_reasons
from utils.applicant_twin import applicant_twin

def approval_trajectory_3d(model, sample, crif_range, foir_range, fixed_salary):
    z_matrix = []

    for crif in crif_range:
        row = []

        for foir in foir_range:
            temp = sample.copy()

            temp["crif_score"] = crif
            temp["true_foir_pct"] = foir
            temp["net_monthly_salary_inr"] = fixed_salary

            prob = model.predict_proba(temp)[0].max() * 100
            row.append(prob)

        z_matrix.append(row)

    return np.array(z_matrix)

# ---------------------------------
# Load Model
# ---------------------------------

model = joblib.load(
    "models/model.pkl"
)

encoder = joblib.load(
    "models/label_encoder.pkl"
)

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="Roopyya AI",
    page_icon="🏦",
    layout="wide"
)

# ---------------------------------
# Header
# ---------------------------------

st.markdown("""
#  Roopyya AI Credit Decision Engine

### AI-Powered Loan Eligibility Assessment Platform
""")

st.divider()

# ---------------------------------
# Input Section
# ---------------------------------

st.subheader(
    "Applicant Information"
)

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        18,
        80,
        29
    )

    crif = st.number_input(
        "CRIF Score",
        300,
        900,
        780
    )

    salary = st.number_input(
        "Monthly Salary (₹)",
        0,
        1000000,
        70000
    )

    job_months = st.number_input(
        "Months In Current Job",
        0,
        500,
        24
    )

with col2:

    loan_amount = st.number_input(
        "Requested Loan Amount (₹)",
        1000,
        5000000,
        150000
    )

    tenure = st.selectbox(
        "Loan Tenure (Days)",
        [90, 180, 270, 365]
    )

    foir = st.slider(
        "FOIR %",
        0,
        100,
        25
    )

    fraud_flag = st.checkbox(
        "Fraud Flag"
    )

    wilful_default = st.checkbox(
        "Wilful Default"
    )

serviceable = st.checkbox(
    "Serviceable Pincode",
    value=True
)

# ---------------------------------
# Analyze
# ---------------------------------

if st.button(
    " Analyze Application"
):

    sample = pd.DataFrame([{
        "age_years": age,
        "crif_score": crif,
        "months_in_current_job": job_months,
        "net_monthly_salary_inr": salary,
        "requested_amount_inr": loan_amount,
        "requested_tenure_days": tenure,
        "true_foir_pct": foir,
        "fraud_flag": int(fraud_flag),
        "wilful_default_flag": int(
            wilful_default
        ),
        "pincode_is_serviceable": int(
            serviceable
        )
    }])

    prediction = model.predict(
        sample
    )

    decision = (
        encoder.inverse_transform(
            prediction
        )[0]
    )

    confidence = float(
        model.predict_proba(
            sample
        ).max()
        * 100
    )
    if confidence >= 95:

        confidence_label = (
            "High Confidence"
        )

    elif confidence >= 80:

        confidence_label = (
            "Medium Confidence"
        )

    else:

        confidence_label = (
            "Borderline Case"
        )

    reasons = generate_reasons(
        crif=crif,
        foir=foir,
        fraud=fraud_flag,
        wilful_default=wilful_default,
        serviceable=serviceable
    )

    twin_score = applicant_twin(
        sample
    )
    health = calculate_credit_health(
    crif,
    salary,
    job_months,
    foir,
    fraud_flag,
    wilful_default,
    serviceable
    )

    recommended_amount, recommendation_text = (
        loan_recommendation(
            decision,
            salary,
            loan_amount,
            foir
        )
    )

    risk_score = round(
        (
            (
                100
                -
                (crif / 9)
            )
            +
            foir
        ) / 2,
        1
    )

    st.divider()

    # -----------------------
    # Decision
    # -----------------------

    st.subheader(
        "Decision Result"
    )

    if decision == "Approved":

        st.success(
            "🟢 GO | APPROVED"
        )

    else:

        st.error(
            "🔴 NOGO | REJECTED"
        )

    # -----------------------
    # Metrics
    # -----------------------

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    with c2:

        st.metric(
            "Risk DNA",
            risk_score
        )

    with c3:

        st.metric(
            "Assessment",
            confidence_label
        )
    # -----------------------
    # Confidence Meter
    # -----------------------

    st.subheader(
        "Confidence Meter"
    )

    st.progress(
        min(
            int(confidence),
            100
        )
    )

    st.write(
        f"Model Confidence: {confidence:.2f}%"
    )

    # -----------------------
    # Risk DNA Gauge
    # -----------------------

    st.subheader(
        "Risk DNA Gauge"
    )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=risk_score,
            title={
                "text":
                "Risk Score"
            },
            gauge={
                "axis":{
                    "range":[0,100]
                }
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -----------------------
    # Applicant Twin
    # -----------------------

    st.subheader(
        "👥 Applicant Twin Analysis"
    )

    st.info(
        f"{twin_score}% of similar applicants were approved."
    )
    st.subheader(
    " Credit Health Radar"
    )

    radar_df = pd.DataFrame(
        {
            "Metric": list(
                health.keys()
            ),
            "Score": list(
                health.values()
            )
        }
    )

    fig_radar = px.line_polar(
        radar_df,
        r="Score",
        theta="Metric",
        line_close=True
    )

    fig_radar.update_traces(
        fill="toself"
    )

    st.plotly_chart(
        fig_radar,
        use_container_width=True
    )

    # -----------------------
    # Reasons
    # -----------------------

    st.subheader(
        "Why This Decision?"
    )

    if len(reasons) >= 1:

        st.error(
            f"Primary Reason: {reasons[0]}"
        )

    if len(reasons) >= 2:

        st.warning(
            f"Secondary Reason: {reasons[1]}"
        )

    if len(reasons) >= 3:

        st.info(
            f"Tertiary Reason: {reasons[2]}"
        )
    st.subheader(
        " Loan Optimization"
    )

    st.info(
        f"""
    Suggested Amount: ₹{recommended_amount:,}

    {recommendation_text}
    """
    )
    # -----------------------
    #  3D Approval Trajectory
    # -----------------------

    st.subheader(" Approval Trajectory (CRIF × FOIR × Salary)")

    st.write(
        "This visualization shows how approval probability changes with CRIF score and FOIR while keeping salary fixed."
    )

    # Fixed salary input
    fixed_salary = st.number_input(
        "Fixed Salary for Simulation (₹)",
        min_value=0,
        max_value=1000000,
        value=int(sample["net_monthly_salary_inr"].iloc[0])
    )

    # Ranges for simulation
    crif_range = np.arange(300, 901, 50)
    foir_range = np.arange(0, 101, 10)

    # Run simulation
    z = approval_trajectory_3d(
        model,
        sample,
        crif_range,
        foir_range,
        fixed_salary
    )

    # 3D Surface Plot
    fig = go.Figure(
        data=[
            go.Surface(
                z=z,
                x=foir_range,
                y=crif_range,
                colorscale="Viridis"
            )
        ]
    )

    fig.update_layout(
        title="Approval Probability Surface (CRIF vs FOIR)",
        scene=dict(
            xaxis_title="FOIR (%)",
            yaxis_title="CRIF Score",
            zaxis_title="Approval Probability (%)"
        ),
        height=700
    )

    st.plotly_chart(fig, use_container_width=True)
    # -----------------------
    # Recommendation
    # -----------------------

    st.subheader(
        "Recommendation"
    )

    if decision == "Approved":

        st.success(
            "Applicant demonstrates a strong credit profile and repayment capacity."
        )

    else:

        st.warning(
            "Review the highlighted risk factors before reconsidering the application."
        )

    # -----------------------
    # Approval Trajectory (2D or 3D)
    # -----------------------

    st.subheader(" Approval Trajectory Analysis")