#########################
# Home work for tomorrow: calculate other evaluation metric
# apart from Accuracy and display them

## Home-work Date: 12thJuly2025
#########################

# ================================
# STEP 1: Import Libraries
# ================================
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# ================================
# STEP 2: Load Dataset
# ================================
url = "https://raw.githubusercontent.com/swapnilsaurav/MachineLearning/refs/heads/master/3_Startups.csv"
df = pd.read_csv(url)

print("Dataset Preview:")
print(df.head())

# ================================
# STEP 3: Convert Categorical Data
# ================================
df = pd.get_dummies(df, drop_first=True)

# ================================
# STEP 4: Create Classification Target
# ================================
df["Profit_Class"] = (df["Profit"] > df["Profit"].median()).astype(int)

# ================================
# STEP 5: Define X and y
# ================================
X_class = df.drop(["Profit", "Profit_Class"], axis=1)
y_class = df["Profit_Class"]

# ================================
# STEP 6: Train-Test Split
# ================================
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    X_class, y_class, test_size=0.2, random_state=42
)

# ================================
# STEP 7: Train Model
# ================================
log_model = LogisticRegression(max_iter=1000)
log_model.fit(Xc_train, yc_train)

# ================================
# STEP 8: Predictions
# ================================
yc_pred = log_model.predict(Xc_test)

# ================================
# STEP 9: Evaluation Metrics
# ================================
accuracy = accuracy_score(yc_test, yc_pred)
precision = precision_score(yc_test, yc_pred)
recall = recall_score(yc_test, yc_pred)
f1 = f1_score(yc_test, yc_pred)
cm = confusion_matrix(yc_test, yc_pred)

# ================================
# STEP 10: Display Results
# ================================
print("\n==============================")
print("   CLASSIFICATION METRICS     ")
print("==============================")

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

print("\nConfusion Matrix:")
print(cm)