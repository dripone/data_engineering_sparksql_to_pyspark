#SparkSQL
LOAD DATA INPATH '/path' INTO TABLE table
INSERT INTO table VALUES (1, 2)
SELECT * FROM table
SAVE AS TABLE table

#PySpark
df = spark.read.csv("/path")
df.write.insertInto("table", overwrite=True)
df = spark.table("table")
df.write.saveAsTable("table", mode="overwrite")
