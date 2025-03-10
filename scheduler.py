import time
import schedule
import database
from datetime import datetime

def check_due_tasks():
    """Fetch tasks from database and check if they are due."""
    tasks = database.get_all_tasks()
    now = datetime.now()

    for task in tasks:
        task_id, title, description, due_date, completed = task

        # Convert string to datetime object
        if isinstance(due_date, str):
            due_date = datetime.strptime(due_date, '%Y-%m-%d %H:%M:%S')

        if not completed and now >= due_date:
            print(f"⚠️ Reminder: Task '{title}' is due! ({due_date})")
            mark_task_completed(task_id)

def mark_task_completed(task_id):
    """Mark a task as completed after sending a reminder."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = TRUE WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Schedule the task checker to run every minute
schedule.every.day.at("23:59").do(check_due_tasks)

if __name__ == "__main__":
    print("📅 Task Scheduler is running... Checking tasks every minute.")
    
    while True:
        schedule.run_pending()
        time.sleep(10)


# Add a condition to stop the scheduler after a certain time or number of runs
run_limit = 5  # Set how many times the loop runs before stopping
run_count = 0

if __name__ == "__main__":
    print("📅 Task Scheduler is running... Checking tasks at 11:59 PM daily.")
    
    while run_count < run_limit:
        schedule.run_pending()  # Run scheduled jobs
        time.sleep(60)  # Sleep for 1 minute to prevent overloading the CPU
        run_count += 1  # Increment the run counter
    
    print("Task Scheduler stopped after reaching the run limit.")