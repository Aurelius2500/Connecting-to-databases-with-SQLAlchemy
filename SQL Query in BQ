# This is the SQL Query as plain text
SELECT COUNT(DISTINCT title) AS number_of_titles,
contributor_id,
FROM `bigquery-public-data.samples.wikipedia`
WHERE is_minor IS NULL
GROUP BY
contributor_id
HAVING number_of_titles > 1000
ORDER BY number_of_titles DESC
