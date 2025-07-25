import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=9010,
    user="postgres",
    password="postgres",
    dbname="tickets"
)
cur = conn.cursor()

cur.execute("""
    INSERT INTO tickets (description, price, date, location) VALUES
    ('Concert A', 50.0, '2025-08-01', 'London'),
    ('Conference B', 120.0, '2025-09-15', 'Berlin'),
    ('Festival C', 75.5, '2025-07-30', 'Paris')
""")
conn.commit()
cur.close()
conn.close()
print("Seeded tickets table.")