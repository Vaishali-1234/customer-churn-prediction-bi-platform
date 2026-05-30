import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

import joblib


# Load dataset
df = pd.read_csv("../data/raw/WA_Fn-UseC_-Telco-Customer-Churn[1].csv")

# Handle TotalCharges
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

# Encode target
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# Encode categorical columns
for col in df.select_dtypes(include=["object", "string"]).columns:
    if col != "customerID":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

# Features and target
X = df.drop(
    columns=[
        "customerID",
        "Churn"
    ]
)

y = df["Churn"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

print(classification_report(
    y_test,
    predictions
))

probs = model.predict_proba(X_test)[:, 1]

print(
    "ROC AUC:",
    roc_auc_score(
        y_test,
        probs
    )
)

# Save model
joblib.dump(
    model,
    "../models/random_forest.pkl"
)
