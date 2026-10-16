
import pandas as pd
from io import StringIO

# Import a small engineering dataset
csv_data = """Sensor,Temperature,Voltage,Current
S1,25.5,3.3,0.12
S2,27.0,3.4,0.15
S3,26.2,3.2,0.11
S4,28.1,3.5,0.18
S5,24.8,3.1,0.10
"""

df = pd.read_csv(StringIO(csv_data))

# Initial data inspection
print("First five rows:")
print(df.head())

print("\nDataset shape:", df.shape)

print("\nColumn names:")
print(list(df.columns))

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Descriptive statistical analysis
print("\nDescriptive statistics:")
print(df.describe().round(2))
