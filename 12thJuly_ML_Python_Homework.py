#######
# Home work: Calculate correlation between each X and y and rerun the model by 
# dropping X which have correlation less than 0.55
# Compare the Rsquare and RMSE values.
##########


# ================================
# STEP 1: Import Libraries
# ================================
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# ================================
# STEP 2: Load Dataset
# ================================
url = "https://raw.githubusercontent.com/swapnilsaurav/MachineLearning/refs/heads/master/3_Startups.csv"
df = pd.read_csv(url)

print("Dataset Preview:")
print(df.head())

# ================================
# STEP 3: Handle Categorical Data
# ================================
df = pd.get_dummies(df, drop_first=True)

# ================================
# STEP 4: Define X and y
# ================================
X = df.drop("Profit", axis=1)
y = df["Profit"]

# ================================
# STEP 5: Correlation Calculation
# ================================
correlation = df.corr()

print("\nCorrelation with Profit:")
print(correlation["Profit"].sort_values(ascending=False))

# ================================
# STEP 6: Select Features (> 0.55)
# ================================
corr_target = correlation["Profit"].abs()

selected_features = corr_target[corr_target > 0.55].index
selected_features = selected_features.drop("Profit")

print("\nSelected Features (corr > 0.55):")
print(selected_features)

X_filtered = df[selected_features]

# ================================
# STEP 7: Train-Test Split
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

Xf_train, Xf_test, yf_train, yf_test = train_test_split(
    X_filtered, y, test_size=0.2, random_state=42
)

# ================================
# STEP 8: Train Model (Original)
# ================================
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# ================================
# STEP 9: Evaluate (Original)
# ================================
r2_original = r2_score(y_test, y_pred)
rmse_original = np.sqrt(mean_squared_error(y_test, y_pred))

# ================================
# STEP 10: Train Model (Filtered)
# ================================
model_f = LinearRegression()
model_f.fit(Xf_train, yf_train)

y_pred_f = model_f.predict(Xf_test)

# ================================
# STEP 11: Evaluate (Filtered)
# ================================
r2_filtered = r2_score(yf_test, y_pred_f)
rmse_filtered = np.sqrt(mean_squared_error(yf_test, y_pred_f))

# ================================
# STEP 12: Compare Results
# ================================
print("\n==============================")
print("        FINAL COMPARISON      ")
print("==============================")

print(f"Original R2   : {r2_original:.4f}")
print(f"Filtered R2   : {r2_filtered:.4f}")

print(f"Original RMSE : {rmse_original:.2f}")
print(f"Filtered RMSE : {rmse_filtered:.2f}")

# ================================
# STEP 13: Conclusion
# ================================
print("\nConclusion:")

if r2_filtered > r2_original and rmse_filtered < rmse_original:
    print("Filtered model is better (Higher R2 & Lower RMSE)")
elif r2_filtered < r2_original and rmse_filtered > rmse_original:
    print("Original model is better")
else:
    print("Both models perform similarly")