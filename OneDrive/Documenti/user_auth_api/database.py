import psycopg

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "gakuhi11360;",
    "host": "localhost",
    "port": 5432,
}
def init_db():
    try:
        with psycopg.connect(**DB_PARAMS) as conn:  
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users( 
                        id SERIAL PRIMARY KEY, 
                        username VARCHAR(50) UNIQUE NOT NULL,
                        email VARCHAR(100) UNIQUE NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """) 
                users = [
                    ("Maxmin", "maxmin@gmail.com"),
                    ("Andrew", "andrew@gmail.com"),
                    ("Selina", "selina@gmail.com"),
                ]
                cur.executemany("""
                     INSERT INTO users (username, email)
                     VALUES (%s, %s)
                     ON CONFLICT (username) DO NOTHING; """,
                     users)  
                conn.commit()
                print("Users table created") 
                cur.execute("SELECT id ,username, email, created_at FROM users;")
                rows = cur.fetchall()

                print ("\nUsers in Database:")
                for row in rows:
                    print(f"ID: {row[0]} | Username: {row[1]} | Email:{row[2]}")
    except Exception as e:
        print(f"Error:{e}")

if __name__ == "__main__":
     init_db()
