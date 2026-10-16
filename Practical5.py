
import pandas as pd

# Create student dataset
data = {
    "RollNo": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Sahil", "Sneha"],
    "Branch": ["ENTC", "Computer", "ENTC", "Computer", "ENTC", "Computer"],
    "Marks": [78, 91, 65, 89, 72, 84]
}

df = pd.DataFrame(data)

# Display student dataset
print("Student dataset:")
print(df)

# Filtering
print("\nStudents scoring 80 or above:")
print(df[df["Marks"] >= 80])

# Sorting
print("\nStudents sorted by marks (highest to lowest):")
print(df.sort_values(by="Marks", ascending=False))

# Conditional selection
print("\nENTC students with marks above 70:")
print(df[(df["Branch"] == "ENTC") & (df["Marks"] > 70)])
