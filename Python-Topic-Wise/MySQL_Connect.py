import mysql.connector

tables = []
table_fields = []

def get_table_name():
    table = input("Enter the table name : ")
    return table

def show_databases():
    cursor.execute("SHOW DATABASES;")
    all_databases = cursor.fetchall()
    print("\n------------------List of Databases------------------\n")
    for database in all_databases:
        print(database)

def show_fields(table_name):
    table_fields.clear()
    desc = describe(table_name)
    for col in desc:
        table_fields.append(col[0])

def execute_tables():
    cursor.execute("SHOW TABLES;")
    all_tables = cursor.fetchall()
    tables.clear()
    for table in all_tables:
        tables.append(table[0])

def show_tables():
    print("\n------------------List of tables------------------\n")
    for table in tables:
        print(table)

def execute_custom_query(prompt):
    try:
        query = input(prompt).strip()
        cursor.execute(query)
    except Exception as e:
        print(f"Error executing query : {e}")

def create_table_query():
    execute_custom_query("Enter the CREATE TABLE query : ")
    print("Table created successfully!\n")
    execute_tables()

def insert_query():
    execute_custom_query("Enter the INSERT query : ")
    print("Values inserted successfully!\n")

def update_query():
    execute_custom_query("Enter the UPDATE query : ")
    print("Table data value updated successfully!\n")

def delete_query():
    execute_custom_query("Enter the DELETE query : ")
    print("Table data deleted successfully!\n")

def select():
    print(f"Tables in your database -->> {tables}")
    table_name = get_table_name()
    if table_name not in tables:
        print("Table does not exist in this database. Kindly check it once :)")
    else:
        show_fields(table_name)
        opt = int(input("Do you want all values(1) or specific values(2) : "))
        desc = describe(table_name)
        if opt == 1:
            query = f"SELECT * FROM {table_name}"
            hasValue = True
        elif opt == 2:
            print(f"Your table has these fields only -->> {table_fields}")
            fields = list(map(str,input("Enter the field names separated by commas: ").split(",")))
            for field in fields:
                if field not in table_fields:
                    print("Field does not exits in this table :) Kindly check it once :)")
                    return
            query = f"SELECT {','.join(fields)} FROM {table_name}"
            hasValue = False
        else:
            print("Choose valuebale option :)")
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            if hasValue:
                print("")
                for col in desc:
                    print(col[0], end="\t\t")
                print("")
                print("")
            else:
                print("")
                for field in fields:
                    print(field,end="\t\t")
                print("")
                print("")

            for row in result:
                for value in row:
                    print(value,end="\t\t")
                print("")
        else:
            print("Table is empty :)")

def describe(table_name):
    cursor.execute(f"DESC {table_name}")
    result = cursor.fetchall()
    desc = []
    for row in result:
        desc.append(row)
    return desc

def truncate_table():
    print(f"Tables in your database -->> {tables}")
    table_name = input("Enter the table name : ")
    if table_name not in [t.lower() for t in tables]:
        print("Table does not exist in this database. Kindly check it once :)")
    else:
        query = f"TRUNCATE TABLE {table_name}"
        cursor.execute(query)
        print(f"TABLE {table_name} IS TRUNCATED SUCCESSFULLY\n")
        execute_tables()

def drop_table():
    print(f"Tables in your database -->> {tables}")
    table_name = input("Enter the table name : ")
    if table_name not in [t.lower() for t in tables]:
        print("Table does not exist in this database. Kindly check it once :)")
    else:
        query = f"DROP TABLE {table_name}"
        cursor.execute(query)
        print(f"TABLE {table_name} IS DROPED SUCCESSFULLY\n")
        execute_tables()

if __name__ == "__main__":
    conn = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "python_mysql")
    cursor = conn.cursor()
    print("Database connected successfully !!!")
    execute_tables()
    while True:
        print("\n------------------Welcome to Python_Mysql Database world------------------")
        print("1. SHOW DATABASES QUERY")
        print("2. SHOW TABLES QUERY")
        print("3. CREATE TABLE QUERY")
        print("4. INSERT QUERY")
        print("5. UPDATE QUERY")
        print("6. DELETE QUERY")
        print("7. SELECT QUERY")
        print("8. DESC QUERY")
        print("9. TRUNCATE TABLE")
        print("10. DROP TABLE")
        print("11. EXIT\n")
        choose = int(input("Choose only one above option (1 TO 11) : "))
        print("")
        if choose == 1:
            show_databases()
            print("")
        elif choose == 2:
            show_tables()
            print("")
        elif choose == 3:
            create_table_query() 
        elif choose == 4:
            insert_query()
        elif choose == 5:
            update_query() 
        elif choose == 6:
            delete_query()  
        elif choose == 7:
            select()   
        elif choose == 8:
            print(f"Tables in your database -->> {tables}")
            table_name = get_table_name()
            if table_name not in [t.lower() for t in tables]:
                print("Table does not exist in this database. Kindly check it once :)")
            else:
                desc = describe(table_name)
                print("\nField\t\tType\n")
                for rows in desc:
                    count = 0
                    for field in rows:
                        print(field,end="\t\t")
                        count += 1
                        if count == 2:
                            break
                    print("")
                print("")
                
        elif choose == 9:
            truncate_table()
            
        elif choose == 10:
            drop_table()
            
        elif choose == 11:
            print("Thank you for using my program :)")
            break
        else:
            print("Invalid option X")
            print("Please choose correct option :)")
            
        conn.commit()