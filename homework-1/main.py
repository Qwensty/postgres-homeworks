"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import psycopg2.errors
from utils import get_data_from_csv


employees = get_data_from_csv('employees_data', 'north_data/employees_data.csv')
customers = get_data_from_csv('customers_data', 'north_data/customers_data.csv')
orders = get_data_from_csv('orders_data', 'north_data/orders_data.csv')

def main():
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='112233'
    )

    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany('INSERT INTO employees_data (first_name, last_name, title, notes)' 'VALUES (%s, %s, %s, %s)', employees)
                cur.executemany('INSERT INTO customers_data VALUES (%s, %s, %s)', customers)
                cur.executemany('INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)', orders)

    except psycopg2.errors.UniqueViolation:
        print("Уже есть в таблице")

    finally:
        conn.close()

if __name__ == '__main__':
    main()