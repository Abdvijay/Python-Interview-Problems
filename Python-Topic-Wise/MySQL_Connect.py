import mysql.connector

tables = []
table_fields = []
databases = []

def get_table_name():
    table = input("Enter the table name : ")
    return table

def show_databases():
    try:
        cursor.execute("SHOW DATABASES;")
        all_databases = cursor.fetchall()
        print("\n------------------List of Databases------------------\n")
        for database in all_databases:
            print(database)
            databases.append(database[0])
    except mysql.connector.Error as e:
            print(f"Error in showing databaes : {e}")

def choose_database():
    while True:
        show_databases()
        database_name = input("\nChoose one database : ")
        print("")
        try:
            if database_name not in databases:
                print("Invalid database entered. Please enter valid database :)")
            else:
                cursor.execute(f"USE {database_name}")
                print("Database connected successfully...!!!")
                execute_tables()
                break
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")

def show_fields(table_name):
    table_fields.clear()
    desc = describe(table_name)
    for col in desc:
        table_fields.append(col[0])

def execute_tables():
    try:
        cursor.execute("SHOW TABLES;")
        all_tables = cursor.fetchall()
        tables.clear()
        for table in all_tables:
            tables.append(table[0])
    except mysql.connector.Error as e:
            print(f"Error in execute tables : {e}")

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
    table_name = get_table_name().strip()
    if table_name not in tables:
        print("Table does not exist in this database. Kindly check it once :)")
    else:
        show_fields(table_name)
        opt = int(input("Do you want all values(1) or specific values(2) : "))
        desc = describe(table_name)
        if opt == 1:
            query = f"SELECT * FROM {table_name}"
            hasValue = True
            cursor.execute(query)
        elif opt == 2:
            print(f"Your table has these fields only -->> {table_fields}")
            fields = list(map(str,input("Enter the field names separated by commas: ").split(",")))
            for field in fields:
                if field not in table_fields:
                    print("Field does not exits in this table :) Kindly check it once :)")
                    return
            query = f"SELECT {','.join(fields)} FROM {table_name}"
            hasValue = False
            cursor.execute(query)
        else:
            print("Choose valuebale option :)")
            return False
        result = cursor.fetchall()
        if result:
            if hasValue:
                print("")
                for col in desc:
                    print(col[0].ljust(15,' '), end="\t")
                print("")
                print("")
            else:
                print("")
                for field in fields:
                    print(field.ljust(15,' '),end="\t")
                print("")
                print("")

            for row in result:
                for value in row:
                    print(str(value).ljust(15,' '),end="\t")
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
    try:
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "1234")
        if conn.is_connected():
            print("Connected to MySQL server successfully...(Without database)!!!")
            cursor = conn.cursor()
            choose_database()
            while True:
                print("\n------------------Welcome to Python_Mysql Database world------------------\n")
                print("1. SHOW DATABASES QUERY")
                print("2. CHANGE DATABASE")
                print("3. SHOW TABLES QUERY")
                print("4. CREATE TABLE QUERY")
                print("5. INSERT QUERY")
                print("6. UPDATE QUERY")
                print("7. DELETE QUERY")
                print("8. SELECT QUERY")
                print("9. DESC QUERY")
                print("10. TRUNCATE TABLE")
                print("11. DROP TABLE")
                print("12. EXIT\n")
                choose = int(input("Choose only one above option (1 TO 12) : "))
                print("")
                if choose == 1:
                    show_databases()
                    print("")
                elif choose == 2:
                    choose_database()
                elif choose == 3:
                    show_tables()
                    print("")
                elif choose == 4:
                    create_table_query() 
                elif choose == 5:
                    insert_query()
                elif choose == 6:
                    update_query() 
                elif choose == 7:
                    delete_query()  
                elif choose == 8:
                    select()   
                elif choose == 9:
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
                                print(field.ljust(15,' '),end="\t")
                                count += 1
                                if count == 2:
                                    break
                            print("")
                        print("")
                        
                elif choose == 10:
                    truncate_table()
                    
                elif choose == 11:
                    drop_table()
                    
                elif choose == 12:
                    print("Thank you for using my program :)")
                    break
                else:
                    print("Invalid option X")
                    print("Please choose correct option :)")
                    
                conn.commit()
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        conn.close()