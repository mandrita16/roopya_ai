def loan_recommendation(
    decision,
    salary,
    requested_amount,
    foir
):

    if decision == "Approved":

        return (
            requested_amount,
            "Requested amount is acceptable."
        )

    max_loan = int(
        salary * 12 * 0.5
    )

    suggested = min(
        requested_amount,
        max_loan
    )

    return (
        suggested,
        "Consider a lower loan amount based on repayment capacity."
    )