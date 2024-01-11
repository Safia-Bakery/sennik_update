import mysql.connector
import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'updates.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Replace these values with your MySQL server details
host = '127.0.0.1'
user = 'root'
password = 'onG89aOkmvPnf'
database = 'safia'

# The search pattern (case-insensitive)

# Establish a connection to MySQL
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL")
        
        for index, row in df.iterrows():
            name = row['Name']
            price = int(row['Price'])
            select_query = "SELECT * FROM entries  WHERE JSON_UNQUOTE(JSON_EXTRACT(data, '$.title')) LIKE %s"
            cursor = connection.cursor(dictionary=True)
            cursor.execute(select_query, ('%' + name + '%',))
            results = cursor.fetchall()
            print(results)
            if results:

                print(f"Found {len(results)} results:")
                # update_query = "UPDATE entries SET column_name = %s WHERE id = %s"
                # new_value = "New Value"
                # row_id_to_update = 1
                # cursor.execute(update_query, (new_value, row_id_to_update))
                # connection.commit()
                # print(f"Updated data for row with id {row_id_to_update}") 

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
