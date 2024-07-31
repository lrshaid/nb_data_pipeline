import pyodbc
import requests as r
import pandas as pd
import json
from sqlalchemy import create_engine
import urllib
import pymssql


login_url='https://api.nb.com.ar/v1/auth/login'
nb_user='RSHA38'
nb_pass='b1wjgp6nTm3'

login_body = {'user':nb_user,'password':nb_pass,'mode':'api'}

response=r.post(login_url,json=login_body)

token=response.json()['token']
token

#products_url='https://api.nb.com.ar/v1/'
products_url='https://api.nb.com.ar/v1/?available_stock=1&brand=LG'
products_auth= {'Authorization':'Bearer '+token}
#products_params=
products_auth
products_response=r.get(products_url,headers=products_auth)

products_response.text

df = pd.read_json(products_response.text,orient='records')


# Connection details
server = 'sobrecodigo-test.database.windows.net'
database = 'dev_2023-06-11T19-20Z'
driver = 'ODBC Driver 18 for SQL Server'
authentication = 'Active Directory Default'  # AD Authentication

# Create a connection string using urllib.quote_plus to escape special characters
connection_string = (
    f"DRIVER={{ {driver} }};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Connection Timeout=30;"
    f"Authentication={authentication};"
)

# URL encode the connection string for SQLAlchemy
encoded_connection_string = urllib.parse.quote_plus(connection_string)

# Create the SQLAlchemy engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={encoded_connection_string}")

# Test the connection
#try:
#    with engine.connect() as connection:
#        result = connection.execute("SELECT @@version;")
#        version = result.fetchone()
#        print(f"SQL Server version: {version[0]}")
#        print("Connection successful!")
#except Exception as e:
#    print(f"An error occurred: {e}")


# Connection details
server = 'sobrecodigo-test.database.windows.net'
database = 'dev_2023-06-11T19-20Z'
username = 'adminsobrecodigo'
password = 'Talar2023'

#try:
#    # Create a connection
#    conn = pymssql.connect(server=server, user=username, password=password, database=database)
#
#    # Create a cursor object using the connection
#    cursor = conn.cursor()
#
#    # Execute a simple query
#    cursor.execute("SELECT @@version;")
#
#    # Fetch the result
#    row = cursor.fetchone()
#    print(f"SQL Server version: {row[0]}")
#
#    # Close the connection
#    conn.close()
#
#    print("Connection successful!")
#except Exception as e:
#    print(f"An error occurred: {e}")
#

df

#df.to_sql('nb.inventory_test', con=conn, if_exists='replace', index=False)