import psycopg2

# PostgreSQL Database Configurations
DB_NAME = "task_db"
DB_USER = "task_user"
DB_PASS = "Password"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            due_date TIMESTAMP,
            completed BOOLEAN DEFAULT FALSE
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def add_task(title, description, due_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, due_date) VALUES (%s, %s, %s)", 
                   (title, description, due_date))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks
