import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        todo_list.append({'task': task, 'completed': False})
        update_listbox()
        entry_task.delete(0, tk.END)

def mark_task_complete():
    selected_index = listbox_tasks.curselection()
    if selected_index:
        index = int(selected_index[0])
        todo_list[index]['completed'] = True
        update_listbox()

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for i, task in enumerate(todo_list):
        status = "✓" if task['completed'] else "○"
        listbox_tasks.insert(tk.END, f"{status} {task['task']}")

root = tk.Tk()
root.title("To-Do List Manager")

todo_list = []

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

entry_task = tk.Entry(frame_input, width=20, font=('Arial', 14))
entry_task.pack(side=tk.LEFT, padx=5)

button_add = tk.Button(frame_input, text="Add", font=('Arial', 12), command=add_task)
button_add.pack(side=tk.LEFT, padx=5)

button_complete = tk.Button(root, text="Mark Complete", font=('Arial', 12), command=mark_task_complete)
button_complete.pack(pady=10)

listbox_tasks = tk.Listbox(root, height=10, width=30, font=('Arial', 14), activestyle="none")
listbox_tasks.pack()

update_listbox()

root.mainloop()
