# **Netflix Customer Service Analysis Project**

## **Netflix Customer Service Analysis Project Objective**
The purpose of this project was to simulate a Netflix Business Analyst role for Customer Service (CS), focusing on analyzing operational metrics to derive actionable insights for improving efficiency and customer satisfaction. This project leverages a real-world dataset to demonstrate data collection, cleaning, modeling, querying, and visualization, culminating in a professional Power BI dashboard.

## **Tools and Technologies Used**
- **SQLite**: For database creation, data querying, and analysis.
- **Excel**: For initial data exploration and basic data cleaning.
- **Python**: For data pipeline automation and transformation.
- **Power BI**: For interactive reporting and visualization.
- **SQL**: For advanced querying and aggregations.

## **Steps Taken**
### **1. Data Collection**
The dataset was sourced from Kaggle. It included customer service data relevant to Netflix operations, such as call durations, satisfaction ratings, costs, and regions.

### **2. Data Cleaning and Preprocessing**
- The dataset was reviewed for missing or inconsistent values using SQLite queries.
- Columns with NULL values were imputed using:
  - Average duration for missing call durations.
  - Average satisfaction rating for null ratings.
- Duplicate rows were identified and removed to ensure data integrity.
- Unnecessary columns were excluded to focus on relevant metrics.

### **3. Data Modeling in SQLite**
- A database named `netflix_cs.db` was created in SQLite.
- The cleaned data was loaded into a table named `customer_service_data`.
- Key queries were executed to:
  - Aggregate data by `Topic`, `Region`, and other metrics.
  - Calculate averages and sums for fields such as `call duration`, `satisfaction rating`, and `cost_per_ticket`.

**Example SQL Query Used**:
```sql
SELECT Topic, region, 
       AVG(duration) AS avg_duration, 
       AVG([Satisfaction rating]) AS avg_rating, 
       AVG(cost_per_ticket) AS avg_cost, 
       COUNT(*) AS total_tickets
FROM customer_service_data
GROUP BY Topic, region;


