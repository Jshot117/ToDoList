
import tkinter as tk
from tkinter import simpledialog
import json
from pathlib import Path
savedListPath = Path("List.json")
backUpPath = Path('backupList.json')

class ToDoList:
    def __init__(self):
        self.items=[]
    def listAddItem(self,description,due_date):
        item = {"description":description,"due_date":due_date}
        self.items.append(item)
    def addItem(self):
        description = simpledialog.askstring('Add To-Do Item', 'Enter the description of the to-do item:')
        due_date = simpledialog.askstring('Add To-Do Item', 'Enter the due date of the to-do item (YYYY-MM-DD):')
        list_box.insert(0, f'{description} ({due_date})')
        self.listAddItem(description,due_date)
    def delete_item(self):
        index = list_box.curselection()[0]
        list_box.delete(index)
    def save_list(self):
        with open('List.json','w') as f:
            json.dump(self.items,f)
        with open('backupList.json','w') as f:
            json.dump(self.items,f)
    def load_list(self):
        if(not savedListPath.exists()):
            self.items = []
        else: 
            with open('List.json', 'r') as f:
                self.items = json.load(f)
    def createList(self):
        if(self.items == 0):
            return
        else:
            for item in todolist.items:
                list_box.insert('end', f'{item["description"]} ({item["due_date"]})')

todolist = ToDoList()            
root = tk.Tk()
root.geometry("600x400")
button = tk.Button(root, text="Add ToDoItem", command=todolist.addItem)
button.pack()

list_box = tk.Listbox()
list_box.pack(fill = 'both', expand = True)

button = tk.Button(text='Delete ToDoItem', command=todolist.delete_item)
button.pack()

todolist.load_list()
todolist.createList()

todolist.save_list()
root.protocol("WM_DELETE_WINDOW", lambda: todolist.save_list())

root.mainloop()
