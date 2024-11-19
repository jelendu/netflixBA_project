import pandas as pd
import sqlite3
import random

# Step 1: Load the original dataset
print("Loading dataset...")
data = pd.read_csv('call_center_data.csv')

# Step 2: Add calculated fields (Cost Per Ticket, Region, Vendor)
print("Enhancing data...")
data['cost_per_ticket'] = [round(random.uniform(5, 50), 2) for _ in range(len(data))]
data['region'] = [random.choice(['APAC', 'EMEA', 'NA', 'LATAM']) for _ in range(len(data))]
data['vendor'] = [random.choice(['Vendor1', 'Vendor2', 'Vendor3']) for _ in range(len(data))]

# Add the duration column from the existing data
print("Adding duration column...")
data['duration'] = data['Speed of answer in seconds']  # Use this column for the duration field

# Step 3: Save the enhanced data as a new CSV file
print("Saving augmented data to 'augmented_data.csv'...")
data.to_csv('augmented_data.csv', index=False)

# Step 4: Connect to the SQLite database (it will create the database if it doesn't exist)
print("Connecting to SQLite database...")
conn = sqlite3.connect('netflix_cs.db')
cursor = conn.cursor()

# Step 5: Create a table for the data
print("Creating table in the database...")
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer_service_data (
    ticket_id TEXT,
    agent_id TEXT,
    duration REAL,
    satisfaction_score REAL,
    cost_per_ticket REAL,
    region TEXT,
    vendor TEXT
)
''')

# Step 6: Insert the data into the database
print("Inserting data into the database...")
data.to_sql('customer_service_data', conn, if_exists='replace', index=False)

# Step 7: Close the connection
conn.close()
print("Data pipeline executed successfully!")
