import sqlite3
import random
import string

# Connect to the database
conn = sqlite3.connect('my_database3.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE my_table (
        id INTEGER PRIMARY KEY,
        nominal_column TEXT,
        ordinal_column TEXT,
        interval_column REAL,
        ratio_column INTEGER,
        foreign_key_column INTEGER,
        compound_key_column      
    )
''')





# Generate and insert random data into the table
for _ in range(1000):
    nominal_data = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    ordinal_data = random.choice(['Low', 'Medium', 'High'])
    interval_data = random.uniform(1.0, 100.0)
    ratio_data = random.randint(1, 100)
    foreign_key_data = random.randint(10000, 20000)
    compound_key_data = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    cursor.execute("INSERT INTO my_table (nominal_column, ordinal_column, interval_column, ratio_column, foreign_key_column, compound_key_column) VALUES (?, ?, ?, ?, ?, ?)", (nominal_data, ordinal_data, interval_data, ratio_data, foreign_key_data, compound_key_data))

# Commit the changes and close the connection
conn.commit()
conn.close()

