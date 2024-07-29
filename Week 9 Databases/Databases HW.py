import sqlite3

connect = sqlite3.connect('Customers.db')
cursor = connect.cursor()
cursor.execute('''
CREATE TABLE customer(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    sales_amount float)''')

cursor.execute('''
INSERT INTO customer (name, email, sales_Amount)
VALUES ('John Doe', 'john.doe@example.com', 1000)
''')
cursor.execute('''
INSERT INTO customer (name, email, sales_Amount)
VALUES ('Jane Smith', 'jane.smith@example.com', 2000)
''')
cursor.execute('''
INSERT INTO customer (name, email, sales_Amount)
VALUES ('Fon Due', 'fon.due@example.com', 3000)
''')

connect.commit()
print("Database created and data inserted successfully\n")

print("All customers")
cursor.execute('SELECT * FROM customer')
results = cursor.fetchall()
print(results)
print()

print("Customers with sales greater than 1000")
cursor.execute('SELECT name, Sales_Amount FROM customer where sales_amount > 1000')
results = cursor.fetchall()
#print(results)
for row in results:
    print(f'{row[0]:15} {row[1]:6}')
print()

min_sales = float(input('Enter the minimum sales: '))
print("Customers with sales greater than ", min_sales)
cursor.execute('SELECT name, sales_Amount FROM customer where sales_amount > ?', (min_sales,))
results = cursor.fetchall()
for row in results:
    print(f'{row[0]:15} {row[1]:6}')
    
connect.close
