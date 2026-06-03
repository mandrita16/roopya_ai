import pandas as pd

df = pd.read_excel("data/Roopyya_Dataset_10000.xlsx")

print("\nCOLUMNS:\n")
print(df.columns.tolist())

print("\nFIRST 5 ROWS:\n")
print(df.head())