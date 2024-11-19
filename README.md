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

## **4. Exporting Data**
The aggregated results were exported to a CSV file using SQLite commands:
- **Export Process**:
  - The `.mode csv` command was used to set the output format to CSV.
  - The `.output summary_report.csv` command directed the query output to a file named `summary_report.csv`.
  - The query results were exported by running:
    ```sql
    SELECT * FROM customer_service_data;
    ```

## **5. Data Visualization with Power BI**
The exported dataset was imported into Power BI Desktop for analysis and visualization.
- **Visualizations Created**:
  - **Bar Chart**: Displaying average call duration by customer issue topics.
  - **Pie Chart**: Highlighting ticket distribution by regions (APAC, NA, LATAM, EMEA).
  - **Card Visuals**: Summarizing total tickets and average ticket costs.
  - **KPI Visuals**: Tracking critical performance metrics like `Sum of avg_cost`.
- **Customization**:
  - Themes and colors were adjusted to ensure clarity and alignment with Netflix's branding.
  - Data interactivity was enabled, allowing users to click on visuals for deeper insights.
  - Filters were added for slicing data by regions and topics.

## **6. Key Business Insights**
Insights derived from the analysis include:
- **Average Call Duration**:
  - Payment-related queries and technical support exhibited slightly higher durations, pointing to potential bottlenecks.
- **Regional Analysis**:
  - Ticket volumes were evenly distributed across regions, suggesting balanced resource allocation.
- **Cost Analysis**:
  - Average costs per ticket offered insights into operational expenses, with opportunities for cost optimization in specific topics.
- **Customer Satisfaction**:
  - High satisfaction ratings (average 68.11%) indicate successful customer engagement but highlight areas for improvement.

## **7. Recommendations**
Based on the insights, the following recommendations were made:
- **Optimize Handling**:
  - Focus on payment-related and technical support queries to reduce call duration and improve efficiency.
- **Cost Efficiency**:
  - Target regions with higher average costs to identify and address inefficiencies.
- **Customer Satisfaction**:
  - Maintain high customer satisfaction while targeting further improvements through additional training and support tools.

## **8. Final Outputs**
- **PDF Report**: A professionally designed dashboard summarizing all key metrics and insights was exported.
- **Power BI Link**: An interactive Power BI report link was generated for stakeholders to explore the data.

## **9. Future Enhancements**
To enhance the analysis further:
- **Automated Pipelines**:
  - Integrate real-time data pipelines using Python for automated data ingestion and transformation.
- **Advanced Modeling**:
  - Add advanced machine learning models to predict ticket trends and forecast satisfaction scores.
