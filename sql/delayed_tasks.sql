
SELECT
    Department,
    COUNT(*) AS Total_Tasks,
    SUM(
        CASE WHEN Delayed = 1 THEN 1 ELSE 0 END
    ) AS Delayed_Tasks,
    ROUND(
        100.0 * SUM(
            CASE WHEN Delayed = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS Delay_Rate
FROM project_tasks
GROUP BY Department
ORDER BY Delayed_Tasks DESC;
