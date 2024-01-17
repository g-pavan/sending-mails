import psycopg2
from datetime import datetime

# Replace these values with your PostgreSQL connection details
db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': '1234',
    'port': '5432',
}

# Replace this with the specific date and time you want to compare
# Year, Month, Day, Hour, Minute, Second
specified_datetime = datetime(2024, 1, 16, 12, 0, 0)

email_list = []
dynamic_values = []

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a SELECT query with a WHERE clause
    query = 'SELECT * FROM public."Employee" WHERE lastmodifieddate > %s;'
    cursor.execute(query, (specified_datetime,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        dynamic_values.append(
            {'name': row[1]+" " + row[2], "employee_id": row[0]})
        email_list.append(row[3])

except psycopg2.Error as e:
    print("Error executing the query:", e)

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")
