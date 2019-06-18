

import psycopg2

# connect to an existing database
try:
    con = psycopg2.connect(
                    host="yhvh",
                    database="python_db",
                    user="postgres",
                    password="ichoose",
                    )
except:
    print("Unable to connect database")

# Open a cursor to perform database operation
cur = con.cursor()

def read(con):
    """
    Read data in Database
    """
    print("Read")

    # execute the query
    data ="SELECT id, name FROM employees"
    cur.execute(
        data
    )
    # fetchall - returns all entries
    rows = cur.fetchall()

    for r in rows:
        print(f"id {r[0]} name {r[1]}")

def create(con, id, name):
    """
    Create data in Database
    """
    print("Create")

    # Insert data
    sql_insert_query = "INSERT INTO employees (id, name) VALUES (%s, %s )"
    cur.execute(
        sql_insert_query,
        (id, name)
    )

    con.commit()
    # see the changes call read(con) function
    read(con)


def update(con, id, name):
    """
    Update Data
    """
    # select data to update
    sql_select_query = 'SELECT * FROM employees WHERE id = %s;'
    cur.execute(
        sql_select_query,
        (id, )
    )
    # print data to update
    record = cur.fetchone()
    print(record)

    # Update single data
    sql_update_query = 'UPDATE employees SET name = %s WHERE id = %s;'
    cur.execute(
        sql_update_query,
        (name, id)
    )
    # print updated data
    count = cur.rowcount
    print(count, "Record Update Succesfully")

    # commit the insert
    con.commit()
    # see the changes
    read(con)

def delete(con, id):
    """
    Delete data in Db
    """
    # query to delete
    sql_delete_query ="DELETE FROM employees WHERE id = %s"
    cur.execute(
        sql_delete_query,
        (id, )
    )
    con.commit()
    # see the changes
    read(con)

read(con)

# # close the cursor
# cur.close()

# # close the connection
# # so it will not be able to link
# con.close()
