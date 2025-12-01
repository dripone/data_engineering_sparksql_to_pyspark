#SparkSQL
SELECT * FROM table
SELECT column1, column2 FROM table
SELECT COUNT(*) FROM table
SELECT DISTINCT column FROM table
SELECT * FROM table WHERE column=value
SELECT * FROM table WHERE column>value
SELECT * FROM table ORDER BY column ASC
SELECT * FROM table ORDER BY column DESC

#PySpark
df.select("*")
df.select("column1", "column2")
df.count()
df.select("column").distinct()
df.filter(df.column == value)
df.filter(df.column > value)
df.orderBy("column", ascending=True)
df.orderBy("column", ascending=False)
