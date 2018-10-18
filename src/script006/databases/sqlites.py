import sqlite3

if __name__ == '__main__':
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    # cursor.execute("Create table table_name(f1 TEXT, f2 TEXT)")
    cursor.execute("""
        INSERT INTO
        table_name
        VALUES ('val1', 'val2'), ('val3', 'val4')"""
        )
    connection.commit()
    cursor.execute("SELECT * from table_name where f1 = ?", ("val1",));
    cursor.execute(
        "SELECT * from table_name where f1 = ?", ("; DROP table table_name;",));
    connection.commit()
    cursor.execute("SELECT * from table_name where f1 = ?", ("val1",));
    result = cursor.fetchall()
    # result = cursor.fetchall()
    print(result)
    # cursor.co

