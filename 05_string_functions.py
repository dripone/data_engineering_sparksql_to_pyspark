#SparkSQL
SELECT UPPER(column) FROM table
SELECT LOWER(column) FROM table
SELECT TRIM(column) FROM table
SELECT SUBSTRING(column, 1, 3) FROM table
SELECT LENGTH(column) FROM table

#PySpark
df.withColumn("column", F.upper(df.column))
df.withColumn("column", F.lower(df.column))
df.withColumn("column", F.trim(df.column))
df.withColumn("column", F.substring(df.column, 1, 3))
df.withColumn("columnLength", F.length(df.column))
