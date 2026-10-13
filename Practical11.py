import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = {
    'Age_Group': ['Young', 'Middle', 'Senior', 'Young', 'Middle', 'Senior', 'Young', 'Middle'],
    'Income': ['High', 'Low', 'Medium', 'Medium', 'High', 'Low', 'Low', 'High'],
    'Student': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes'],
    'Purchased': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

X = df.drop(columns=['Purchased'])
y = df['Purchased']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

categorical_features = ['Age_Group', 'Income', 'Student']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

model_pipeline = Pipeline(
    steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression())
    ]
)

model_pipeline.fit(X_train, y_train)

y_pred = model_pipeline.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

