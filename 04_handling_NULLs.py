#SparkSQL
SELECT * FROM table WHERE column IS NULL
SELECT * FROM table WHERE column IS NOT NULL
SELECT column, COALESCE(column, 0) FROM table
SELECT column, IFNULL(column, 0) FROM table

#PySpark
df.filter(df.column.isNull())
df.filter(df.column.isNotNull())
df.withColumn("column", F.coalesce(df.column, F.lit(0)))
"df.withColumn(""column"", F.when(df.column.isNull(), 0)
.otherwise(df.column))"
