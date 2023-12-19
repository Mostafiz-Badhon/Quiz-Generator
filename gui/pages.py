import tkinter as tk
from tkinter import ttk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='green')

        self.controller = controller
        # To paint the modules.
        self.button_F1 = tk.Button(self, text='F1', command=lambda: self.controller.display_frame(ModulePage))
        self.button_F1.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.button_F2 = tk.Button(self, text='F2', command=lambda: print("pressed F2"))
        self.button_F2.grid(column=1, row=0, sticky=tk.NSEW, padx=10, pady=10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)


class ModulePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='red')
        self.controller = controller

        # inform label
        self.title_label = tk.Label(self, text='AVAILABLE MODULES FOR QUIZ')
        self.title_label.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW, padx=10, pady=10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.up_buttom = tk.Button(self, text='MODULES', command=lambda: controller.show_frame(StartPage))
        self.up_buttom.grid(row=0, column=0, sticky='nswe', padx=10, pady=10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # using a treeview
        # 4 line protocol
        self.treeview = ttk.Treeview(self, selectmode='browse', columns=('NAME', 'DESCRIPTION'), show='headings',
                                     style="mystyle.Treeview")
        self.treeview.grid(row=1, column=0, columnspan=4, sticky=tk.NSEW, padx=10, pady=10)
        self.rowconfigure(1, weight=5)
        self.columnconfigure(0, weight=1)

        self.treeview.heading('NAME', text='NAME')
        self.treeview.heading('DESCRIPTION', text='DESCRIPTION')

        #  binding module_selected
        self.treeview.bind('<<TreeviewSelect>>', self.treeview_select)
        self.treeview.bind('<Double-1>', self.treeview_double_1)

        # using an scroll bar
        # 4 line protocol
        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.treeview.yview)
        scrollbar.grid(row=1, column=4, sticky=tk.NSEW)
        self.rowconfigure(1, weight=25)
        self.columnconfigure(1, weight=1)

        # linking
        self.treeview.configure(yscroll=scrollbar.set)

        name_label = tk.Label(self, text=" Name :")
        name_label.grid(row=2, column=0, sticky=tk.NSEW, padx=10, pady=10)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        self.name_entry = tk.Entry(self, textvariable=tk.StringVar())
        self.name_entry.grid(row=2, column=1, sticky=tk.NSEW, padx=10, pady=10)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)

        description_label = tk.Label(self, text=" Description :")
        description_label.grid(row=2, column=2, sticky=tk.NSEW, padx=10, pady=10)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(2, weight=1)

        self.description_entry = tk.Entry(self, textvariable=tk.StringVar())
        self.description_entry.grid(row=2, column=3, sticky=tk.NSEW, padx=10, pady=10)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Buttonery for command actions contained in an auxiliar pannel.
        self.button_Frame = tk.Frame(self, bg='lightblue')
        self.button_Frame.grid(row=1, column=5, columnspan=1, rowspan=1, sticky=tk.NSEW, padx=10, pady=10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(5, weight=1)

        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(6, weight=1)

        add_button = tk.Button(self.button_Frame, bg='cyan', text="Add", command=lambda: self.add_row())
        add_button.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)
        self.button_Frame.rowconfigure(0, weight=1)
        self.button_Frame.columnconfigure(0, weight=1)

        remove_button = tk.Button(self.button_Frame, bg='cyan', text="Remove", command=lambda: self.remove_row())
        remove_button.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)
        self.button_Frame.rowconfigure(1, weight=1)
        self.button_Frame.columnconfigure(0, weight=1)

        edit_button = tk.Button(self.button_Frame, bg='cyan', text="Edit", command=lambda: self.edit_row())
        edit_button.grid(row=2, column=0, sticky=tk.NSEW, padx=10, pady=10)
        self.button_Frame.rowconfigure(2, weight=1)
        self.button_Frame.columnconfigure(0, weight=1)

        exit_button = tk.Button(self.button_Frame, bg='cyan', text="Exit", command=lambda: print("to do"))
        exit_button.grid(row=3, column=0, sticky=tk.NSEW, padx=10, pady=10)
        self.button_Frame.rowconfigure(3, weight=1)
        self.button_Frame.columnconfigure(0, weight=1)

        # geting data from DDBB
        # controller
        for module in self.controller.get_Modules_from_db():
            self.treeview.insert('', tk.END, values=(module.name, module.description))
            print(module.description, module.name)

    def treeview_select(self, event):
        # Fill in the contents.
        selected_modules = self.treeview.selection()
        print(selected_modules)
        # assert (len(selected_modules) == 1)
        for selected_row in selected_modules:
            selected_row = self.treeview.item(selected_modules[0])
            name, description = selected_row['values'][0], selected_row['values'][1]
            print(name, description)
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.description_entry.delete(0, tk.END)
            self.description_entry.insert(0, description)

    def treeview_double_1(self, event):
        # Fill in the contents.
        selected_modules = self.treeview.selection()
        assert len(selected_modules) == 1
        selected_row = self.treeview.item(selected_modules[0])
        code = selected_row['values'][0]
        print('RAFA', code)
        self.controller.show_frame(StartPage, code)

    def add_row(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        self.treeview.insert('', tk.END, values=(name, description))
        self.controller.add_Module_to_db((name, description))

    def remove_row(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        self.treeview.insert('', tk.END, values=(name, description))
        self.controller.remove_Module_from_db((name, description))

    def edit_row(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        self.treeview.insert('', tk.END, values=(name, description))
        self.controller.edit_Module_from_db((name, description))


