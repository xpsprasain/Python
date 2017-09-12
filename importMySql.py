__author__ = 'sulav'

import pymysql

# define the credentials and database details
HOSTNAME = 'localhost'
USER = 'root'
PW = ''
TABLE = 'test_table'
DB = 'test'

insert_queries = []

# establish connection
conn = pymysql.connect(host=HOSTNAME, user=USER, password=PW, db=DB)


def insert_records():
    """
    This method inserts data to the connected database and selected table from above variables
    User provides the data to enter as per users' desire
    Queries are stored in list which are inserted one by one
    If any issue occurs then the connection is rolled back
    """
    choice = 'Y'

    while (choice.lower() == 'y'):
        name = input("Enter name")
        address = input("Enter address")
        position = input("Enter position")
        salary = int(input("Enter salary"))
        insert_queries.append(prepare_insert_query(TABLE, name, address, position, salary))

        choice = input("Want to insert another(Y/N)")

    try:
        with conn.cursor() as cursor:  # creating cursor object2
            for insert in insert_queries:
                print("query=" + insert)
                cursor.execute(insert)  # executing query

        conn.commit()  # commit changes
    except Exception as error:
        print(error)
        conn.rollback()  # rollback in case of error


def see_records():
    """
    This method is to display records on terminal
    """
    print("{0:<20}{1:20}{2:<20}{3:<10}".format("name", "address", "position", "salary"))
    print("----------------------------------------------------------------------")
    with conn.cursor() as cursor:
        cursor.execute("select * from {}".format(TABLE))
        allRecords = cursor.fetchall()
        for i in allRecords:
            print("{0:<20}{1:<20}{2:<20}{3:<10}".format(i[1], i[2], i[3], i[4]))


def prepare_insert_query(table=None, name=None, address=None, position=None, salary=None):
    return "insert into {0}(name, address, position, salary) values ('{1}','{2}','{3}',{4})".format(table, name,address,position, salary)


def create_tbl_stmt():
    return "create table if not exists {0}" \
           "(id int(20) NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(20), " \
           "address varchar(20), position varchar(20), salary float(20));".format(TABLE)


def create_table():
    print(create_tbl_stmt())

    with conn.cursor() as cursor:
        cursor.execute(create_tbl_stmt())


def delete_record():
    """
    This method is to delete record by matching name
    Progress is checked according ro result variable
    If the value of result varibale is greater than 0 then it is successful else it fails
    """
    del_name = input("Enter name to be deleted")

    query = "delete from {0} where name='{1}'".format(TABLE, del_name)

    result = None

    try:
        with conn.cursor() as cursor:
            result = cursor.execute(query)

        conn.commit()
    except Exception as error:
        print(error)
        conn.rollback()
        # fucntion of rollback is past state

    if (result != 1):
        print("Cannot delete. Make sure your query is correct")


def update_name():
    """
    This method is to update old_name by new_name
    Progress is checked according ro result variable
    If the value of result varibale is greater than 0 then it is successful else it fails
    """

    old_name = input("Enter the name to be replaced")
    new_name = input("Enter the name to be replaced with")

    result = None

    query = "update {} set name='{}' where name = '{}'".format(TABLE, new_name, old_name)

    try:
        with conn.cursor() as cursor:
            result = cursor.execute(query)
    except Exception as error:
        print(error)
        conn.rollback()

    conn.commit()

    if result != 1:
        print("Cannot update. Make sure your query is correct")


def main():
    create_table()

    print("Select Option\n1.Insert Records\n2.See all Records\n3.Delete Records\n4.Update Name")
    user_choice = input("Enter your choice")
    if user_choice == '1':
        insert_records()
    elif user_choice == '2':
        see_records()
    elif user_choice == '3':
        delete_record()
    elif user_choice == '4':
        update_name()
    else:
        print("Wrong choice")

    conn.close()


if __name__ == '__main__':
    main()