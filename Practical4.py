
import pandas as pd
from io import StringIO

# Student dataset
data = """RollNo,Name,Branch,Marks,City
101,Amit,ENTC,78,Pune
102,Neha,Computer,,
103,Rahul,ENTC,65,Mumbai
103,Rahul,ENTC,65,Mumbai
104,Priya,Computer,89,
105,Sahil,ENTC,72,Nashik
"""

df = pd.read_csv(StringIO(data))

# Display original dataset
print("Original dataset:")
print(df)

# Fill missing marks with the average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing city with "Unknown"
df["City"] = df["City"].fillna("Unknown")

# Remove duplicate rows
df = df.drop_duplicates()

# Rename columns
df = df.rename(columns={
    "RollNo": "Roll_No",
    "Marks": "Exam_Marks"
})

# Round marks to one decimal place
df["Exam_Marks"] = df["Exam_Marks"].round(1)

# Change column order
df = df[["Roll_No", "Name", "Branch", "City", "Exam_Marks"]]

# Display preprocessed dataset
print("\nPreprocessed dataset:")
print(df.to_string(index=False))

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Display number of rows
print("\nNumber of rows after removing duplicates:", len(df))
