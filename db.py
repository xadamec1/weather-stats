""" This file is responsible for managing access to sqlite DB"""
import datetime
import os

import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        try:
            create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            print(f"Table '{table_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table '{table_name}': {e}")

    def insert_weather(self, data):
        try:
            placeholders = ', '.join(['?'] * len(data))
            insert_sql = f"INSERT INTO weather (url, temperature, weather_date) VALUES ({placeholders})"
            self.cursor.execute(insert_sql, data)
            self.conn.commit()
            print("Data inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")

    def query_data(self, table_name, condition=None):
        try:
            query_sql = f"SELECT * FROM {table_name}"
            if condition:
                query_sql += f" WHERE {condition}"
            self.cursor.execute(query_sql)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Error querying data: {e}")
            return []

    def close_connection(self):
        self.conn.close()
        print("Database connection closed.")


class PlaceEntity:
    def __init__(self, name, country, gps_latitude=0.0, gps_longitude=0.0):
        self.name = name
        self.gps_latitude = gps_latitude
        self.gps_longitude = gps_longitude
        self.country = country


def initialize_db():
    os.remove("weather.db")
    db = Database("weather.db")

    # Create a table
    table_name = "weather"
    weather_columns = ["id INTEGER PRIMARY KEY", "url TEXT", "temperature FLOAT, weather_date DATETIME"]
    db.create_table(table_name, weather_columns)

    place_columns = ["id INTEGER PRIMARY KEY, name TEXT, latitude FLOAT, longitude FLOAT, country TEXT"]
    db.create_table("places", place_columns)
    # Insert data
    data1 = ("www.example-weather.com/today", "35.5", datetime.date.today())
    data2 = ("www.basic-weather.com/today", "34.5", datetime.date.today())

    db.insert_weather( data1)
    db.insert_weather( data2)

    # Query data
    result = db.query_data(table_name)
    for row in result:
        print(row)

    # Close the database connection
    db.close_connection()


if __name__ == "__main__":
    initialize_db()
