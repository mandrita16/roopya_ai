import pandas as pd

from sklearn.neighbors import NearestNeighbors

df = pd.read_excel("data/Roopyya_Dataset_10000.xlsx")

features = [
    "age_years",
    "crif_score",
    "months_in_current_job",
    "net_monthly_salary_inr",
    "requested_amount_inr",
    "true_foir_pct"
]

X = df[features]

nn = NearestNeighbors(
    n_neighbors=50
)

nn.fit(X)

sample = [[
    29,
    780,
    24,
    70000,
    150000,
    25
]]

distances, indices = nn.kneighbors(sample)

similar_people = df.iloc[indices[0]]

approved_pct = (
    (similar_people["loan_status"]=="Approved")
    .mean()
    *100
)

print(
    f"Applicant Twin Found. Similar approvals: {approved_pct:.2f}%"
)