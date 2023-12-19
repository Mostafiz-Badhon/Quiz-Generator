import sqlite3

db_path = "C:\\Users\\mosta\\PycharmProjects\\pythonProject2\\res\\questions"


def drop_table(table):
    con = sqlite3.connect(db_path)
    questions = "drop table " + table
    con.execute(questions)
    con.close()

def populate_questions_table():
    con = sqlite3.connect(db_path)
    "\
     create table if not exists QUESTIONS (\
     NAME text ,\
     NO integer,\
     HEADER text,\
     TYPE text\
    )"

    insert_questions = "insert into questions values(?,?,?,?)"
    # 10 questions
    for i in range(10):
        con.execute(insert_questions, ("COMP181" + str(i), i, 'Header' + str(i) + str(i), 'TRUE OR FALSE'))
        con.commit()
        con.close()
        return
