
import pandas as pd

# Create student dataset
data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Sahil", "Sneha"],
    "Department": ["ENTC", "Computer", "ENTC", "Computer", "ENTC", "Computer"],
    "Marks": [78, 91, 65, 89, 72, 84]
}

df = pd.DataFrame(data)

# Display student dataset
print("Student dataset:")
print(df)

# Group data by department and calculate summary values
summary = df.groupby("Department").agg(
    Total_Marks=("Marks", "sum"),
    Average_Marks=("Marks", "mean"),
    Student_Count=("Name", "count")
)

# Round average marks to one decimal place
summary["Average_Marks"] = summary["Average_Marks"].round(1)

# Display department-wise summary
print("\nDepartment-wise summary:")
print(summary)

# Find the highest marks in each department
highest = df.groupby("Department")["Marks"].max()

print("\nHighest marks in each department:")
print(highest)
