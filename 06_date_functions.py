#SparkSQL
SELECT CURRENT_DATE()
SELECT CURRENT_TIMESTAMP()
SELECT YEAR(column) FROM table
SELECT MONTH(column) FROM table
SELECT DAY(column) FROM table
SELECT DATEDIFF(end_date, start_date) FROM table

#PySpark
df.withColumn("current_date", F.current_date())
df.withColumn("current_timestamp", F.current_timestamp())
df.withColumn("year", F.year(df.column))
df.withColumn("month", F.month(df.column))
df.withColumn("day", F.dayofmonth(df.column))
df.withColumn("date_diff", F.datediff(df.end_date, df.start_date))
