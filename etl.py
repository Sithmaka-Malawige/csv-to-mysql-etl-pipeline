import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv(r"C:\Users\DELL\Documents\DEpractice\ETL-Pipeline\data\clean_sales.csv")
print(df.columns.tolist())

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="sales_db"
)

cursor = conn.cursor()
print("Connected to MySQL")

for index, row in df.iterrows():
    sql = """
    INSERT INTO sales
    (Order_ID,Product,Category,Price,Quantity,Revenue)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    values = (
        row["Order ID"],
        row["Item Type"],
        row["Sales Channel"],   
        row["Unit Price"],
        row["Units Sold"],
        row["Total Revenue"]
    )
    cursor.execute(sql, values)

conn.commit()
print("Data inserted successfully")