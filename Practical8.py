import matplotlib.pyplot as plt
import seaborn as sns
#from Practical_8 import correlation_matrix

df=sns.load_dataset("penguins")
print(df.head(10))
df = df.dropna()
print(df.head(10))
print(df.info())

plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
)

plt.title("Scatter Plot : Bill Length vs Bill Depth ")
plt.xlabel("Bill Length")
plt.ylabel("Bill Depth")
plt.show()

plt.figure(figsize=(6,5))
numeric_data = df.select_dtypes(include="number")
correlation_matrix = numeric_data.corr()

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="Greens",
    fmt =".2f",
)
plt.title("Correlation Heatmap")
plt.show()