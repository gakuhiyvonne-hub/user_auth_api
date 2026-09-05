'''import requests

response = requests.get("https://api.restful-api.dev/objects")
data = response.json()
print(data)'''

import requests 
import pandas as pd
response = requests.get("https://api.restful-api.dev/objects")
data = response.json()
df = pd.DataFrame(data)
print(f"Columns:")
print(df.columns.tolist())
print(f"\nRows:{len(df)}")
print("\nFirst 3 rows:")
print(df.head(3))
df_clean = df.dropna(subset=['data'])
print(f"Rows before leaing: {len(df)}")
print(f"Rows after cleaning:{len(df_clean)}")
print(df_clean)