from google.cloud import bigquery

project = 'kew-science' # Project ID inserted based on the query results selected to explore
location = 'US' # Location inserted based on the query results selected to explore
client = bigquery.Client(project=project, location=location)
sql = """
-- What specimens represent taxa that have less than 15 specimens?
SELECT
  gbifID,
  taxonkey,
  scientificName,
  eventDate,
  countryCode
FROM
  `bigquery-public-data.gbif.occurrences`
WHERE
  taxonkey IS NOT NULL
  AND phylum = 'Tracheophyta'
  AND basisofrecord = 'PRESERVED_SPECIMEN'
QUALIFY
  COUNT(*) OVER (PARTITION BY taxonkey) < 15;
"""

# Run a Standard SQL query using the environment's default project
df = client.query(sql).to_dataframe()
print(df)