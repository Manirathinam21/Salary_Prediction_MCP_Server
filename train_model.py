import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error

#Load_Dataset
df = pd.read_csv('data.csv')

# Features and Target
X = df.drop('market_salary_lpa', axis=1)
y= df['market_salary_lpa']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),   
    ('model', RandomForestRegressor(
        n_estimators=200,
        max_depth=6, 
        random_state=42
        ))
])

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions
y_pred = pipeline.predict(X_test)

# Evaluate the model
print("\nModel Performance:")
print("R2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

# Save the trained model
joblib.dump(pipeline, './salary_model.pkl')

print("\nModel saved as 'salary_model.pkl'")
