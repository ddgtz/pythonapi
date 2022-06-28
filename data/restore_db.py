"""

    Run this to restore the database, if needed.

"""
import csv
from pathlib import Path
import sqlite3

resources = [
    {
        'data_file': 'celebrity_100.csv',
        'drop_stmt': 'DROP TABLE IF EXISTS celebrity',
        'create_stmt': 'CREATE TABLE IF NOT EXISTS celebrity (id integer primary key autoincrement, Name VARCHAR(100), Pay REAl, Year VARCHAR(15), Category VARCHAR(50))',
        'insert_stmt': 'INSERT INTO celebrity(Name, Pay, Year, Category) VALUES (?,?,?,?)'
    },
    {
        'data_file': 'customer_purchases.csv',
        'drop_stmt': 'DROP TABLE IF EXISTS purchases',
        'create_stmt': 'CREATE TABLE purchases (id integer primary key autoincrement, InvoiceNo VARCHAR(30) NOT NULL, StockCode VARCHAR(30) NOT NULL, Quantity INTEGER NOT NULL, Description VARCHAR(150), InvoiceDate VARCHAR(50), UnitPrice REAL, CustomerID VARCHAR(50), Country VARCHAR(50))',
        'insert_stmt': 'INSERT INTO purchases(InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country) VALUES (?,?,?,?,?,?,?,?)'
    },
    {
        'data_file': 'netflix_titles.csv',
        'drop_stmt': 'DROP TABLE IF EXISTS netflix_titles',
        'create_stmt': 'CREATE TABLE IF NOT EXISTS netflix_titles (show_id VARCHAR(10) NOT NULL PRIMARY KEY, type VARCHAR(20), title VARCHAR(60), director VARCHAR(50), cast VARCHAR(250), country VARCHAR(40), date_added VARCHAR(40), release_year VARCHAR(10), rating VARCHAR(10), duration VARCHAR(20), listed_in VARCHAR(250), description VARCHAR(500))',
        'insert_stmt': 'INSERT INTO netflix_titles(show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
    },
    {
        'data_file': 'richest_athletes.csv',
        'drop_stmt': 'DROP TABLE IF EXISTS athletes',
        'create_stmt': 'CREATE TABLE IF NOT EXISTS athletes (SNo VARCHAR(10) NOT NULL PRIMARY KEY, Name VARCHAR(60), Nationality VARCHAR(25), CurrentRank VARCHAR(10), PreviousYearRank VARCHAR(20), Sport VARCHAR(50), Year VARCHAR(15), Earnings REAL)',
        'insert_stmt': 'INSERT INTO athletes(SNo, Name, Nationality, CurrentRank, PreviousYearRank, Sport, Year, Earnings) VALUES (?,?,?,?,?,?,?,?)'
    },
    {
        'data_file': 'users.csv',
        'drop_stmt': 'DROP TABLE IF EXISTS users',
        'create_stmt': 'CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY autoincrement, name VARCHAR(80) NOT NULL, username VARCHAR(80) NOT NULL, email VARCHAR(120) NOT NULL UNIQUE, password VARCHAR(250) NOT NULL)',
        'insert_stmt': 'INSERT INTO users(id,name,username,email,password) VALUES (?,?,?,?,?)'
    },
    {
        'data_file': 'user_auth.csv',
        'drop_stmt': 'DROP TABLE IF EXISTS user_auth',
        'create_stmt': 'CREATE TABLE IF NOT EXISTS user_auth (id integer not null primary key autoincrement, public_id varchar, name varchar, password varchar, admin boolean)',
        'insert_stmt': 'INSERT INTO user_auth(id, public_id, name, password, admin) VALUES (?,?,?,?,?)'
    }
]


def create_db_table(data_file: str, drop_stmt: str, create_stmt: str, insert_stmt: str, has_header: bool = True):
    db_file = 'course_data.db'
    data_file = Path(data_file)
    data = []
    try:
        with open(data_file, mode='rt', encoding='unicode_escape') as f:
            print(f'\nReading data file: {data_file}')
            try:
                reader = csv.reader(f)
                for row in reader:
                    data.append(row)
            except (UnicodeDecodeError, csv.Error) as err:
                print(f'Data reading error: {err}.  Problem occurred on line: {reader.line_num}.')
    except IOError as err:
        print(f'IOError: {err}')
        return

    print(f'File read complete: {data_file}')
    if has_header:
        data = data[1:]

    connection = None
    try:
        print(f'Database {db_file} opened')
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute(drop_stmt)
        print('--> Table dropped')
        cursor.execute(create_stmt)
        print('--> New table created')
        cursor.executemany(insert_stmt, data)
        print('--> Data Inserted')
        connection.commit()
        print(data_file.stem, f'data loaded into {db_file}')
    except sqlite3.Error as err:
        if connection:
            connection.rollback()
        print('Warning: ', data_file.stem, f'data NOT loaded into {db_file}')
        print('Database Error: {0}'.format(err))
    finally:
        if connection:
            connection.close()
            print(f'Database {db_file} closed')


for resource in resources:
    create_db_table(resource.get('data_file'),
                    resource.get('drop_stmt'),
                    resource.get('create_stmt'),
                    resource.get('insert_stmt'))
