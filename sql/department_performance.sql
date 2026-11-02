
SELECT
    Department,
    COUNT(*) AS Total_Tasks,
    SUM(CASE WHEN Status = 'Completed' THEN 1 ELSE 0 END)
        AS Completed_Tasks,
    ROUND(
        100.0 * SUM(CASE WHEN Status = 'Completed' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Completion_Rate
FROM project_tasks
GROUP BY Department
ORDER BY Completion_Rate DESC;
