# -*- coding: utf-8 -*-
"""CA1-Kumar_Dange-10637925.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eNIPXuLHfRNznX0MUP2w7yB4c7tSe66-

# **CA1 PROJECT**
"""

# loading libraries 
import requests
import json
#import pandas as pd
pandas

url = 'https://www.arnotts.ie/content/arnotts/ie/en/plp/jcr:content/root/container/plpcontainer.json?pagePath=https://www.arnotts.ie/men/shoes/&q%3Dmenu%3Dtrue%26offset%3D36%26limit%3D36&siteID=arnotts'

data = 'pagePath=https://www.arnotts.ie/men/shoes/&q%3Dmenu%3Dtrue%26offset%3D36%26limit%3D36&siteID=arnotts'

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en,en-IN;q=0.9',
    'cookie': 'expires_in=1800; token_type=BEARER; responseCode=200; sessionType=guest; usid=79fd6f30-37c8-4486-bbb4-36970ec704b5; customer_id=belXJKxcxKkXaRkXBHmbYYlcE0; OptanonAlertBoxClosed=2024-11-28T00:25:10.648Z; _gcl_au=1.1.1315704018.1732753511; _ga=GA1.1.361626742.1732753511; _fbp=fb.1.1732753511167.188889357489442709; _pin_unauth=dWlkPU1qTTFZbUZoTURNdFl6STBZaTAwWVRKaUxUbG1PVEF0TnpJNE4yWmlOREJrTVdJNQ; _tt_enable_cookie=1; _ttp=ckx5KOdImWde9f4GxGHMSqgyhrk.tt.1; affinity="1512366832c6029e"; currency=EUR; access_token=eyJ2ZXIiOiIxLjAiLCJqa3UiOiJzbGFzL3Byb2QvYmJicF9wcmQiLCJraWQiOiI4Y2FkNjkxMy1kNzEzLTRhYTgtOThlNS01N2I3MzcxN2IwZTUiLCJ0eXAiOiJqd3QiLCJjbHYiOiJKMi4zLjQiLCJhbGciOiJFUzI1NiJ9.eyJhdXQiOiJHVUlEIiwic2NwIjoic2ZjYy5zaG9wcGVyLW15YWNjb3VudC5iYXNrZXRzIHNmY2MuY2F0YWxvZ3Mgc2ZjYy5zaG9wcGVyLWRpc2NvdmVyeS1zZWFyY2ggc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wYXltZW50aW5zdHJ1bWVudHMgc2ZjYy5zaG9wcGVyLWN1c3RvbWVycy5sb2dpbiBzZmNjLm9yZGVycyBzZmNjLnNob3BwZXItbXlhY2NvdW50Lm9yZGVycyBzZmNjLnByb2R1Y3RzIHNmY2Muc2hvcHBlci1wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLXByb21vdGlvbnMgc2ZjYy5vcmRlcnMucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wYXltZW50aW5zdHJ1bWVudHMucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLWNhdGVnb3JpZXMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudCBzZmNjLnNob3BwZXItbXlhY2NvdW50LmFkZHJlc3NlcyBzZmNjLnNob3BwZXItcHJvZHVjdHMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5ydyBzZmNjLmN1c3RvbWVybGlzdHMucncgc2ZjYy5zaG9wcGVyLXN0b3JlcyBzZmNjLnByb2R1Y3RzLnJ3IHNmY2Muc2hvcHBlci1iYXNrZXRzLW9yZGVycyBzZmNjLnNob3BwZXItY3VzdG9tZXJzLnJlZ2lzdGVyIHNmY2MuY2F0YWxvZ3Mucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5hZGRyZXNzZXMucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wcm9kdWN0bGlzdHMucncgc2ZjYy5zaG9wcGVyLWJhc2tldHMtb3JkZXJzLnJ3IHNmY2Muc2hvcHBlci1wcm9kdWN0LXNlYXJjaCBzZmNjLmN1c3RvbWVybGlzdHMiLCJzdWIiOiJjYy1zbGFzOjpiYmJwX3ByZDo6c2NpZDozYTM4OWIwYS00NzdjLTRhZWEtODRiMi0xZjE5MWJjNjg5OGQ6OnVzaWQ6NzlmZDZmMzAtMzdjOC00NDg2LWJiYjQtMzY5NzBlYzcwNGI1IiwiY3R4Ijoic2xhcyIsImlzcyI6InNsYXMvcHJvZC9iYmJwX3ByZCIsImlzdCI6MSwiZG50IjoiMCIsImF1ZCI6ImNvbW1lcmNlY2xvdWQvcHJvZC9iYmJwX3ByZCIsIm5iZiI6MTczMzQ5OTgyMSwic3R5IjoiVXNlciIsImlzYiI6InVpZG86c2xhczo6dXBuOkd1ZXN0Ojp1aWRuOkd1ZXN0IFVzZXI6OmdjaWQ6YmVsWEpLeGN4S2tYYVJrWEJIbWJZWWxjRTA6OmNoaWQ6YXJub3R0cy1nbG9iYWwiLCJleHAiOjE3MzM1MDE2NTEsImlhdCI6MTczMzQ5OTg1MSwianRpIjoiQzJDMTMzMzgyNTYzNzAtMTA0MjQ3MzQ1MjEyMzQ3NzI2NjY0NDc1MjU1In0.bXEJcRKeTvzbEFf1mvgIo8mntjDhWGUdAYwdL7VSjJtGzsf3tqwiybkCoW84jpA_RGZp4RtE0kCR3ofIDpl7dg; refresh_token=uIV4YLvOZRCfenfkgmjuYV1cHZ5V-xwHH7JJ42ekaJ0; pg_cnt=NaN; OptanonConsent=isIABGlobal=false&datestamp=Fri+Dec+06+2024+15%3A44%3A37+GMT%2B0000+(Greenwich+Mean+Time)&version=6.10.0&hosts=&consentId=27a90ba3-20fd-4e8f-8fd2-fb3eaa83db15&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=%3B&AwaitingReconsent=false; rr_rcs=eF4NybERgDAIBdAmlbv8u2BIgA2cIwTuLOzU-fW1r2zXe5-rkg0BSWtspsLdGogBKo8fu6-IzInZM8Ck_l8wUgYvrzrV5AOXBBKl; _ga_27S4VCR20B=GS1.1.1733499855.14.1.1733499886.0.0.1431363492',
    'priority': 'u=1, i',
    'referer': 'https://www.arnotts.ie/men/shoes/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

r=requests.get(url, headers=headers)

r

r.content

j=json.loads(r.content)
# json = data is same as data=json.dumps(data)
# data = data means json=json.loads(data)

j.keys()

pd.json_normalize(j['products'])

"""# **Feature Extraction**"""

arnots_df = pd.json_normalize(j['products'])
print('Data types of each feature of arnots_df\n',arnots_df.dtypes)

# Removing unnecessary and empty features
arnots_df = arnots_df.drop(columns=['images','productType','variation-type','energy-rating','c_isdropship','c_isconcession','productcollection','product-label.label-text','product-label.label-text-color','product-label.label-background-color','product-label'], errors='ignore') #Empty data

arnots_df.head()

for i in arnots_df.columns:
    print(f'Length of unique values in {i} is', len(arnots_df[i].apply(lambda x: str(x) if isinstance(x, (list, dict)) else x).unique()))

# changing the columns names
arnots_df.rename(columns={
    'c_primaryCategoryId': 'primaryCategoryID',
    'c_parentPLU': 'parentPLU',
    'brand': 'brandName',
    'price': 'originalPrice',
    'variation-count': 'variationCount',
    'product_id': 'productID',
    'product_name': 'productName',
    'sale-price': 'salePrice'
}, inplace=True)

arnots_df

"""# **Data Transformation**"""

# Checking null vaules in the features table
null_count = arnots_df.isnull().sum()
print('Null values in the each feature:\n', null_count)

# Handle missing values
arnots_df['salePrice'] = arnots_df['salePrice'].fillna(0) # Fill missing with 0(Zero)

# Verifying missing values after handling
arnots_cleaned = arnots_df.isnull().sum()
print('Null values in the each feature after handling:\n',arnots_cleaned)

arnots_df.head()

print('Data types of each feature of arnots_df\n', arnots_df.dtypes)

import re
import pandas as pd

# Compact function for processing price values
process_price=lambda x: (sum(map(float, re.findall(r"\d+\.\d+", str(x)))) / 2) if '-' in str(x) else pd.to_numeric(x, errors='coerce')

# Apply the function to clean 'original_price' before type conversion
arnots_df['originalPrice'] = arnots_df['originalPrice'].apply(process_price)

# Defining the column types
column_types = {
    'primaryCategoryID': str,
    'parentPLU': str,
    'brandName': str,
    'originalPrice': float,  # Now this should work correctly
    'salePrice': float,
    'variationCount': int,
    'productID': str,
    'productName': str
}

# Loop through the DataFrame columns and converting them based on the expected data types
for column in arnots_df.columns:
    if column in column_types:
        arnots_df[column] = arnots_df[column].astype(column_types[column])

# updated data types to confirm the changes
print(arnots_df.dtypes)

# updated DataFrame
arnots_df.head()



# Adding new feature; Discount percentage.
# Calculate discount percentage
arnots_df['discountPercentage'] = ((arnots_df['originalPrice'] - arnots_df['salePrice']) / arnots_df['originalPrice']) * 100

# Round the discount percentage to 2 decimal places and append '%'
arnots_df['discountPercentage'] = arnots_df['discountPercentage'].round(2).astype(str) + '%'

# Adding nw feature; more purchased brand.
# Calculting the brand name counts
brandName_counts = arnots_df['brandName'].value_counts()

# Map brand names to their counts to create the new feature
arnots_df['mostPopularityBrand'] = arnots_df['brandName'].map(brandName_counts)

# data rFame after adding the new features
arnots_df

arnots_df.brandName.unique()

arnots_df

"""### **Data Visualization of Features**"""

# plotting distribution of brand_name in pie chart

#loading necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Setting theme
sns.set_theme(style="whitegrid")

# Plot the distribution of 'brand_name' in a pie chart
plt.figure(figsize=(8, 8))
arnots_df['brandName'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Brand Name Distribution')
plt.ylabel('')  # Hide the 'y' label for aesthetics
plt.show()

# bar plot: Top 10 band_name distribution

# Count the occurrences of each brand and get the top 10
top_brands = arnots_df['brandName'].value_counts().head(10)

# Create the bar plot
plt.figure(figsize=(10, 6))
top_brands.plot(kind='bar', color='skyblue')

# Set plot title and labels
plt.title('Top 10 Brand Name Distribution')
plt.xlabel('Brand Name')
plt.ylabel('Count')
plt.xticks(rotation=45)

# Display the plot
plt.show()

#Visualize Distributions of Numerical Columns

# Setting theme
sns.set_theme(style="whitegrid")

# Plot histograms for numerical columns
numerical_columns = arnots_df.select_dtypes(include=['float64', 'int64']).columns

plt.figure(figsize=(10, 8))
for i, col in enumerate(numerical_columns, 1):
    plt.subplot(2, 2, i)
    sns.histplot(arnots_df[col], kde=True, bins=20, color='blue')
    plt.title(f'Distribution of {col}')
plt.xlabel(col)
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter plot: Sale price vs. Discount percentage
plt.figure(figsize=(8, 6))
sns.scatterplot(data=arnots_df, x='discountPercentage', y='salePrice', hue='brandName', palette='tab10')
plt.title('Sale Price vs Discount Percentage')
plt.xlabel('Discount Percentage')
plt.ylabel('Sale Price')
plt.legend(title='Brand', loc='upper right', bbox_to_anchor=(1.3, 1))
plt.tight_layout()
plt.show()

print('Data types of each feature \n',arnots_df.dtypes)
arnots_df.head()

arnots_df_3 = arnots_df

"""# Loading the Data"""
import sqlite3
import pandas as pd  # Import pandas
from flask import Flask, render_template, request, json, Response
from flask_cors import CORS

# Database Connection
connection = sqlite3.connect('arnots_3.db', check_same_thread=False)
cursor = connection.cursor()
arnots_df_3.to_sql('arnots_data_2', connection, if_exists='append', index=False)
cursor = connection.cursor()

cursor.execute("SELECT * FROM arnots_data_3")
rows = cursor.fetchall()
rows

# Flask App Initialization
app = Flask(__name__)
CORS(app)

# Default Route - Show Data
@app.route("/base.html")
def base():
    return render_template("base.html")

# Route to Add Shoes
@app.route("/addShoes", methods=['GET', 'POST'])
def addShoes():
    if request.method == 'POST':
        # Fetch form data
        primaryCategoryID = request.form.get('primaryCategoryID')
        parentPLU = request.form.get('parentPLU')
        brandName = request.form.get('brandName')
        originalPrice = request.form.get('originalPrice')
        variationalCount = request.form.get('variationalCount')
        productID = request.form.get('productID')
        productName = request.form.get('productName')
        salePrice = request.form.get('salePrice')
        discountPercentage = request.form.get('discountPercentage')
        mostPopularityBrand = request.form.get('mostPopularityBrand')

        # Insert into the database safely
        cursor.execute("""
            INSERT INTO arnots_data_3 (
                primaryCategoryID, parentPLU, brandName, originalPrice, 
                variationalCount, productID, productName, salePrice, 
                discountPercentage, mostPopularityBrand
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            primaryCategoryID, parentPLU, brandName, originalPrice, 
            variationalCount, productID, productName, salePrice, 
            discountPercentage, mostPopularityBrand
        ))
        connection.commit()

        return '{"Result":"Success"}'
    else:
        return render_template('addShoes.html')

# Route to Get Shoes Data
@app.route("/getShoes", methods=['GET'])
def getShoes():
    cursor.execute("SELECT * FROM arnots_data_3")
    rows = cursor.fetchall()

    Results = []
    for row in rows:
        Results.append({
            'primaryCategoryID': row[0],
            'parentPLU': row[1],
            'brandName': row[2],
            'originalPrice': row[3],
            'variationalCount': row[4],
            'productID': row[5],
            'productName': row[6],
            'salePrice': row[7],
            'discountPercentage': row[8],
            'mostPopularityBrand': row[9]
        })

    response = {
        'Results': Results,
        'count': len(Results)
    }

    return Response(json.dumps(response), status=200, mimetype='application/json')

# Run the Flask App
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, ssl_context=('cert.pem', 'privkey.pem'))