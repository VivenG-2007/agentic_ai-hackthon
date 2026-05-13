import sqlite3
query = "SELECT * FROM users WHERE id = ?"
try:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query, (user_id,))
    # rest of the code...
except sqlite3.Error as e:
    print(f"An error occurred: {e}")