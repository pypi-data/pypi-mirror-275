import tkinter as tk
from datetime import datetime

def add_task():
    task = entry_task.get()
    deadline = entry_deadline.get()
    if task:
        current_time = datetime.now().strftime("%m-%d")  # Adjusted format
        task_with_time = f"{task} │ {deadline} │ {current_time}"
        listbox_tasks.insert(tk.END, task_with_time)
        listbox_tasks.insert(tk.END, "-"*80)  # Insert a separator line
        entry_task.delete(0, tk.END)
        entry_deadline.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.delete(selected_task_index)  # Delete the separator line as well
    except IndexError:
        pass

def edit_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task, deadline, _ = listbox_tasks.get(selected_task_index)
        entry_task.delete(0, tk.END)
        entry_task.insert(0, task)
        entry_deadline.delete(0, tk.END)
        entry_deadline.insert(0, deadline)
        delete_task()
    except IndexError:
        pass

def toggle_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(selected_task_index, bg="lightgrey")
    except IndexError:
        pass

root = tk.Tk()
root.title("ToDo List")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_task = tk.Label(frame_input, text="Task:")
label_task.grid(row=0, column=0)

entry_task = tk.Entry(frame_input, width=30)
entry_task.grid(row=0, column=1)

label_deadline = tk.Label(frame_input, text="Deadline:")
label_deadline.grid(row=0, column=2)

entry_deadline = tk.Entry(frame_input, width=20)
entry_deadline.grid(row=0, column=3)

button_add_task = tk.Button(root, text="Add Task", width=10, command=add_task)
button_add_task.pack(side=tk.LEFT, padx=5)

button_edit_task = tk.Button(root, text="Edit Task", width=10, command=edit_task)
button_edit_task.pack(side=tk.LEFT, padx=5)

button_delete_task = tk.Button(root, text="Delete Task", width=10, command=delete_task)
button_delete_task.pack(side=tk.LEFT, padx=5)

button_toggle_task = tk.Button(root, text="Toggle Completed Task", width=20, command=toggle_task)
button_toggle_task.pack(pady=10)

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=80)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

root.mainloop()
