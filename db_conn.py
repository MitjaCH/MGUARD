import mysql.connector

def on_connect():
    try:
        db_config = {
            'host': 'host',
            'port': 'port',
            'user': 'username',
            'password': 'user_password',
            'database': 'database_name'
        }

        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print("Connected to MySQL database")

        return connection

    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None
