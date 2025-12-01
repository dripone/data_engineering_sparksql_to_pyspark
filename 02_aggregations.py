#SparkSQL
SELECT COUNT(column) FROM table
SELECT MAX(column) FROM table
SELECT MIN(column) FROM table
SELECT AVG(column) FROM table
SELECT SUM(column) FROM table
SELECT column, COUNT(*) FROM table GROUP BY column
SELECT column, SUM(column2) FROM table GROUP BY column
SELECT column, AVG(column2) FROM table GROUP BY column
SELECT column, MIN(column2) FROM table GROUP BY column

#PySpark
df.agg(F.count("column").alias("count"))
df.agg(F.max("column").alias("max"))
df.agg(F.min("column").alias("min"))
df.agg(F.avg("column").alias("avg"))
df.agg(F.sum("column").alias("sum"))
df.groupBy("column").agg(F.count("*").alias("count"))
df.groupBy("column").agg(F.sum("column2").alias("sum"))
df.groupBy("column").agg(F.avg("column2").alias("avg"))
df.groupBy("column").agg(F.min("column2").alias("min"))
