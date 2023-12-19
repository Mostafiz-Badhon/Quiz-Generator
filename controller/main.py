import sqlite3
import tkinter as tk

from gui.pages import StartPage, ModulePage
from model.entities_obj import Module

db_path = "C:\\Users\\mosta\\PycharmProjects\\pythonProject2\\res\\quizz.sqlite3"


def edit_Module_from_db(row):
    conn = sqlite3.connect(db_path)
    edit_statement = "EDIT INTO MODULES VALUES (?,?)"
    conn.execute(edit_statement, row)
    conn.commit()
    conn.close()

def remove_Module_from_db(row):
    conn = sqlite3.connect(db_path)
    remove_statement = "REMOVE INTO MODULES VALUES (?,?)"
    conn.execute(remove_statement, row)
    conn.commit()
    conn.close()


class App(tk.Tk):
    def __init__(self, *args, **kwags):
        tk.Tk.__init__(self, *args, **kwags)
        # container
        # 4 lines
        container = tk.Frame(self, bg='yellow')
        container.grid(row=0, column=0, sticky='nswe', padx=10, pady=10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.deck = {}
        for F in (StartPage,ModulePage):
            # 4 line protocol
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky='nswe', padx=10, pady=10)
            container.rowconfigure(0, weight=1)
            container.columnconfigure(0, weight=1)
            self.deck[F] = frame

        self.display_frame(StartPage)

    def display_frame(self, cont):
        frame = self.deck[cont]
        frame.tkraise()

    def get_Modules_from_db(self):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM MODUlES")
        results = []
        for i in cursor.fetchall():
            print('MOSTAFIZUR', i)
            results.append(Module(i))

        return results

    def add_Module_to_db(self, row):
        conn = sqlite3.connect(db_path)
        insert_statement = "INSERT INTO MODULES VALUES (?,?)"
        conn.execute(insert_statement, row)
        conn.commit()
        conn.close()

    def remove_Module_from_db(self, row):
        conn = sqlite3.connect(db_path)
        remove_statement = "REMOVE INTO MODULES VALUES (?,?)"
        conn.execute(remove_statement, row)
        conn.commit()
        conn.close()


app = App()
app.state('zoomed')
app.mainloop()
