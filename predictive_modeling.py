import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sqlite3

# Step 1: Load the enhanced data from the SQLite database
print("Loading data from the database...")
conn = sqlite3.connect('netflix_cs.db')
# Use the correct column name from the database and alias it as 'satisfaction_score'
query = "SELECT duration, [Satisfaction rating] AS satisfaction_score, cost_per_ticket FROM customer_service_data"
data = pd.read_sql_query(query, conn)

# Step 2: Prepare data for predictive modeling
print("Preparing data for modeling...")
X = data[['duration', 'satisfaction_score']]  # Features
y = data['cost_per_ticket']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the linear regression model
print("Training the predictive model...")
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions
print("Making predictions...")
predictions = model.predict(X_test)

# Save predictions to a CSV file
output = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
output.to_csv('predictions.csv', index=False)
print("Predictions saved to 'predictions.csv'.")

# Close the database connection
conn.close()
