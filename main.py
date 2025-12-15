import pandas as pd

# Load the CSV
df = pd.read_csv("UpdatedMetaData.csv")

# Print headers top-down
for col in df.columns:
    print(col)