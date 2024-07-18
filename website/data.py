import json
import os
import mysql.connector

# Load JSON data
with open(r'C:\Users\chill\OneDrive\Documents\Project\shades.json', 'r') as file:
    data = json.load(file)

# Connect to MySQL
conn = mysql.connector.connect(
    host=os.getenv('localhost'),
    user=os.getenv('satya2302'),
    password=os.getenv('Siri_2302'),
    database=os.getenv('my_database')
)
cursor = conn.cursor()

# Insert data into table
for record in data:
    cursor.execute("""
        INSERT INTO my_table (brand,brand_short,product,product_short,hex,H,S,V,L,`group`,shade)
        VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (record['brand'], record['brand_short'], record['product'],record['product_short'],record['hex'],record['H'].record['s'],record['v'],record['l'],record['group'],record['shade']))

# Commit and close
conn.commit()
cursor.close()
conn.close()
