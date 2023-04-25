import csv

def get_data_from_csv(key: str, path:str):
    """Считывает строки из файла"""
    with open(path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        if key == 'employees_data':
            for row in reader:
                first_name = row['first_name']
                last_name = row['last_name']
                profession = row['title']
                description = row['notes']
                data.append((first_name, last_name, profession, description)) #кортеж

        elif key == 'customers_data':
            for row in reader:
                customer_id = row['customer_id']
                company_name = row['company_name']
                contact = row['contact_name']
                data.append((customer_id, company_name, contact)) #кортеж

        elif key == 'orders_data':
            for row in reader:
                order_id = row['order_id']
                customer_id = row['customer_id']
                employee_id = row['employee_id']
                order_date = row['order_date']
                ship_city = row['ship_city']
                data.append((order_id, customer_id, employee_id, order_date, ship_city))


        return data