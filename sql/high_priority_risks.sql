
SELECT
    Department,
    City,
    COUNT(*) AS At_Risk_Tasks
FROM project_tasks
WHERE At_Risk = 1
GROUP BY Department, City
ORDER BY At_Risk_Tasks DESC;
