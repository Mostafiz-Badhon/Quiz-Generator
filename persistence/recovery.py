import sqlite3

db_path = "C:\\Users\\mosta\\PycharmProjects\\pythonProject2\\res\\quizz.sqlite3"

def drop_table(table):
    con = sqlite3.connect(db_path)
    statement = "drop table " + table
    con.execute(statement)
    con.close()

def populate_module_table():
    con = sqlite3.connect(db_path)
    statement = "CREATE TABLE IF NOT EXISTS MODULES ( " \
                "  NAME  TEXT," \
                "  DESCRIPTION TEXT )"
    con.execute(statement)

    insert_statement = "INSERT INTO MODULES VALUES (?,?)"
    # 10 modules
    for i in range(10):
        con.execute(insert_statement, ("COMP181" + str(i), "description for ""COMP181" + str(i)))
    con.commit()
    con.close()
    return




