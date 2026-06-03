import pandas as pd
from sklearn.neighbors import NearestNeighbors

df = pd.read_excel(
    "data/Roopyya_Dataset_10000.xlsx"
)

FEATURES = [
    "age_years",
    "crif_score",
    "months_in_current_job",
    "net_monthly_salary_inr",
    "requested_amount_inr",
    "true_foir_pct"
]

X = df[FEATURES]

nn = NearestNeighbors(
    n_neighbors=50
)

nn.fit(X)


def applicant_twin(sample_df):

    distances, indices = nn.kneighbors(
        sample_df[FEATURES]
    )

    similar = df.iloc[
        indices[0]
    ]

    approved_pct = (
        (
            similar["loan_status"]
            ==
            "Approved"
        ).mean()
        * 100
    )

    return round(
        approved_pct,
        2
    )