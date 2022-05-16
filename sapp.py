import psycopg2

url = "postgres://ytvgpoub:Tk01c0hREg23DLdnD5d8enDIw8CcKEH4@arjuna.db.elephantsql.com/ytvgpoub"
connection = psycopg2.connect(url)
cursor = connection.cursor()
cursor.execute("select * from users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()