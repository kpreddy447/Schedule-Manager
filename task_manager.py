import database
import datetime
import schedule
import time

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def save(self):
        database.add_task(self.title, self.description, self.due_date)
        print("Task added successfully!")

def get_user_input():
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    due_date = input("Enter Due Date (YYYY-MM-DD HH:MM): ")
    return Task(title, description, due_date)

def schedule_reminder(task):
    schedule.every().day.at(task.due_date.split(" ")[1]).do(lambda: print(f"Reminder: {task.title} is due!"))

if __name__ == "__main__":
    database.init_db()
    new_task = get_user_input()
    new_task.save()
    
    all_tasks = database.get_all_tasks()
    print("\nAll Tasks:")
    for task in all_tasks:
        print(task)

    schedule_reminder(new_task)
    
    while True:
        schedule.run_pending()
        time.sleep(10)