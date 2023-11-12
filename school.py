

import sqlite3
import random
import string

# Connect to the database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create a table
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

cursor.execute('''
    CREATE TABLE student (
        id INTEGER,
        name_nominal_column TEXT,
        gender_ordinal_column TEXT,
        percentage_interval_column REAL,
        year_ratio_column INTEGER,
        compound_key_column,
        course_id INTEGER,
        FOREIGN KEY (course_id) REFERENCES course(course_id),
        PRIMARY KEY (id, name_nominal_column)
    )
''')


# Generate and insert random data into the table
for num in range(1000):
    name_nominal_data = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    gender_ordinal_data = random.choice(['Male', 'Female'])
    percentage_interval_data = random.uniform(50.0, 100.0)
    year_ratio_data = random.randint(1990, 2000)
    compound_key_data = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    course_id_data = random.randint(1, 1000)
    cursor.execute("INSERT INTO student (id, name_nominal_column, gender_ordinal_column, percentage_interval_column, year_ratio_column, compound_key_column, course_id) VALUES (?, ?, ?, ?, ?, ?, ?)", (num, name_nominal_data, gender_ordinal_data, percentage_interval_data, year_ratio_data, compound_key_data, course_id_data))


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

