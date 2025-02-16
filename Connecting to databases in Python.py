# -*- coding: utf-8 -*-
"""
Connecting to databases with SQLAlchemy
Spyder version 5.3.3
"""

# In this video, We will connect to Big Query using SQLAlchemy
# You will need to use pip install sqlalchemy-bigquery if you don't have it installed yet
# We will also need pandas to store the results into a dataframe

import sqlalchemy
import pandas as pd

# Set the default dilaect to Big Query, as SQL alchemy can connect to multiple databses
sqlalchemy.dialects.registry.register('bigquery', 'sqlalchemy_bigquery', 'BigQueryDialect')

# We will need to create an engine
# You will also need to create a JSON credential file for your account
# Replace the file with the path to your own account and file
engine = sqlalchemy.create_engine(
    'bigquery://',
    credentials_path = "C:/Users/andre/Downloads/analytics-mindset-3d8f85e55c7a.json",
)

# This part creates the connection
connection = engine.connect()

# Here we put the actual query that we want to execute
query = sqlalchemy.text("""SELECT COUNT(DISTINCT title) AS number_of_titles,
contributor_id,
FROM `bigquery-public-data.samples.wikipedia`
WHERE is_minor IS NULL
GROUP BY
contributor_id
HAVING number_of_titles > 1000
ORDER BY number_of_titles DESC""")

# Create the results object by executing the query
result = connection.execute(query)

# We could print out each line
for row in result:
    print(row)

# Or store it into a pandas dataframe
with engine.connect() as connection:
    df = pd.read_sql_query(query, connection)

# See the resulting dataframe
df.head(10)

# It is good practice to then close the connection
connection.close()
