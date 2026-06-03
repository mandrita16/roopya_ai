def generate_reasons(
    crif,
    foir,
    fraud,
    wilful_default,
    serviceable
):

    reasons = []

    if fraud:
        reasons.append(
            "Fraud flag detected - automatic risk trigger"
        )

    if wilful_default:
        reasons.append(
            "Previous wilful default history found"
        )

    if crif < 650:
        reasons.append(
            f"Credit score ({crif}) is below preferred threshold"
        )

    if foir > 60:
        reasons.append(
            f"FOIR ({foir}%) indicates excessive debt burden"
        )

    if not serviceable:
        reasons.append(
            "Applicant location is not serviceable"
        )

    if len(reasons) == 0:
        reasons.append(
            "Strong credit profile and repayment capacity"
        )

    return reasons