import mysql.connector

def on_connect():
    try:
        db_config = {
            'host': '-',
            'port': '-',
            'user': '-',
            'password': '-',
            'database': '-'
        }

        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print("Connected to MySQL database")

        return connection

    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

def load_users():
    connection = on_connect()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM user")
            users = cursor.fetchall()
            return [user[0] for user in users]

        except mysql.connector.Error as error:
            print("Error loading users:", error)

        finally:
            connection.close()

    return []



def register_user(username, password, email):
    connection = on_connect()
    if connection:
        try:
            cursor = connection.cursor()

            query = "INSERT INTO user (name, password, email) VALUES (%s, %s, %s)"
            values = (username, password, email)

            cursor.execute(query, values)
            connection.commit()

            print("User registered successfully.")

        except mysql.connector.Error as error:
            print("Error registering user:", error)
            connection.rollback()

        finally:
            connection.close()

def get_password(username):
    connection = on_connect()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT password FROM user WHERE name = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                return result[0]  # Returning the stored password
        except mysql.connector.Error as error:
            print("Error fetching password:", error)
        finally:
            connection.close()
    return None