import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure the screenshots folder exists
from pathlib import Path

Path("../screenshots").mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv("../data/raw/WA_Fn-UseC_-Telco-Customer-Churn[1].csv")

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nChurn Distribution:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print((df["Churn"].value_counts(normalize=True) * 100).round(2))

print("\nContract vs Churn:")
print(pd.crosstab(df["Contract"], df["Churn"]))

print("\nPayment Method vs Churn:")
print(pd.crosstab(df["PaymentMethod"], df["Churn"]))

print("\nAverage Tenure by Churn:")
print(df.groupby("Churn")["tenure"].mean())

print("\nAverage Monthly Charges by Churn:")
print(df.groupby("Churn")["MonthlyCharges"].mean())

# Chart 1: Churn distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.savefig("../screenshots/churn_distribution.png", bbox_inches="tight")
plt.close()

# Chart 2: Contract analysis
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Contract", hue="Churn")
plt.xticks(rotation=15)
plt.title("Contract vs Churn")
plt.savefig("../screenshots/contract_churn.png", bbox_inches="tight")
plt.close()

# Chart 3: Payment method analysis
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="PaymentMethod", hue="Churn")
plt.xticks(rotation=30, ha="right")
plt.title("Payment Method vs Churn")
plt.savefig("../screenshots/payment_method_churn.png", bbox_inches="tight")
plt.close()