#SparkSQL
SELECT * FROM table1 JOIN table2 ON condition
SELECT * FROM table1 LEFT JOIN table2 ON condition
SELECT * FROM table1 RIGHT JOIN table2 ON condition
SELECT * FROM table1 FULL JOIN table2 ON condition

#PySpark
df1.join(df2, on="condition", how="inner")
df1.join(df2, on="condition", how="left")
df1.join(df2, on="condition", how="right")
df1.join(df2, on="condition", how="outer")
