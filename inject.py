import sqlite3

def search_users(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Vulnerable query - directly concatenating user input into the SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    users = cursor.fetchall()

    for user in users:
        print(user)

    conn.close()

if __name__ == "__main__":
    search_users("admin';--")
