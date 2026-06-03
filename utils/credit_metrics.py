def calculate_credit_health(
    crif,
    salary,
    job_months,
    foir,
    fraud,
    wilful_default,
    serviceable
):

    credit_strength = min(
        max((crif - 300) / 600 * 100, 0),
        100
    )

    income_stability = min(
        ((salary / 100000) * 70)
        +
        ((job_months / 60) * 30),
        100
    )

    repayment_capacity = max(
        100 - foir,
        0
    )

    location_score = (
        100 if serviceable else 20
    )

    compliance_score = 100

    if fraud:
        compliance_score -= 50

    if wilful_default:
        compliance_score -= 50

    compliance_score = max(
        compliance_score,
        0
    )

    return {
        "Credit Strength": round(
            credit_strength, 1
        ),
        "Income Stability": round(
            income_stability, 1
        ),
        "Repayment Capacity": round(
            repayment_capacity, 1
        ),
        "Location Eligibility": round(
            location_score, 1
        ),
        "Risk Compliance": round(
            compliance_score, 1
        )
    }