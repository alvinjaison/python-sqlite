# python-sqlite

This Python program generates an SQLite database, creates a table, and populates it with 1000 rows of random data.

## Prerequisites

- Linux/Mac (Not tested on Windows)
- Python 3. [Installation instructions](https://www.python.org/downloads/)
- SQLite database installed. [Installation guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-sqlite-on-ubuntu-20-04)

## Usage

1. Clone this repository to your local machine:
   git clone https://github.com/alvinjaison/python-sqlite.git
css
2. Navigate to the cloned repository directory:
   cd python-sqlite
   
4. Run the code to create the database. The database will be created in the same directory with the name `my_database.db`:
  python3 main.py

5. Load the database using the SQLite shell:
   sqlite3 ./my_database.db
   
6. List the databases, and it will show the database `my_database.db` with its absolute path:
.database

7. List the tables, and you will see the `my_table` there:
.tables

8. Run a SELECT command to view the data in the table:
SELECT * FROM my_table;

