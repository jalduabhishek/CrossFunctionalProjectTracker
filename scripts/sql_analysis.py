
import pandas as pd
import sqlite3

# Load project dataset
df = pd.read_csv("data/project_tasks.csv")

# Connect to SQLite database
conn = sqlite3.connect("data/project_tracker.db")

# Store dataset in SQL table
df.to_sql(
    "project_tasks",
    conn,
    if_exists="replace",
    index=False
)

# Execute SQL query
query = """
SELECT
    Department,
    COUNT(*) AS Total_Tasks,
    SUM(CASE WHEN Status = 'Completed' THEN 1 ELSE 0 END)
        AS Completed_Tasks,
    SUM(CASE WHEN Delayed = 1 THEN 1 ELSE 0 END)
        AS Delayed_Tasks
FROM project_tasks
GROUP BY Department
ORDER BY Total_Tasks DESC;
"""

result = pd.read_sql_query(query, conn)

print("SQL DATABASE CREATED SUCCESSFULLY!")
print("\nDEPARTMENT-WISE PROJECT PERFORMANCE")
print(result.to_string(index=False))

conn.close()
