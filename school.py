

import sqlite3
import random
import string

# Connect to the database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE student (
        id INTEGER PRIMARY KEY,
        name_nominal_column TEXT,
        gender_ordinal_column TEXT,
        percentage_interval_column REAL,
        year_ratio_column INTEGER,
        scholarship_foreign_key_column INTEGER,
        compound_key_column      
    )
''')

cursor.execute('''
    CREATE TABLE course (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT,
        instructor TEXT,
        credit REAL,
        difficulty TEXT,
        fee INTEGER,
        duration INTEGER   
    )
''')




# Generate and insert random data into the table
for _ in range(1000):
    name_nominal_data = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    gender_ordinal_data = random.choice(['Male', 'Female'])
    percentage_interval_data = random.uniform(50.0, 100.0)
    year_ratio_data = random.randint(1990, 2000)
    scholarship_foreign_key_data = random.randint(10000, 20000)
    compound_key_data = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    cursor.execute("INSERT INTO student (name_nominal_column, gender_ordinal_column, percentage_interval_column, year_ratio_column, scholarship_foreign_key_column, compound_key_column) VALUES (?, ?, ?, ?, ?, ?)", (name_nominal_data, gender_ordinal_data, percentage_interval_data, year_ratio_data, scholarship_foreign_key_data, compound_key_data))


# Generate and insert random data into the table
for _ in range(1000):
    course_name_data = random.choice(['science', 'cloud', 'data', 'mba', 'ibm'])
    instructor_data = random.choice(['Prof. Andrew', 'Prof. Smith', 'Prof. Jake', 'Prof. Smith', 'Prof. Milan', 'Prof. Alvin'])
    credit_data = random.uniform(20.0, 30.0)
    difficulty_data = random.choice(['easy', 'intermediate', 'difficult', 'very difficult'])
    fee_data = random.choice(['25000', '24000', '30000', '27000', '35000'])
    duration_data = random.choice(['1 year', '2 year', '3 year'])
    cursor.execute("INSERT INTO course (course_name, instructor, credit, difficulty, fee, duration) VALUES (?, ?, ?, ?, ?, ?)", (course_name_data, instructor_data, credit_data, difficulty_data, fee_data, duration_data))


# Commit the changes and close the connection
conn.commit()
conn.close()

