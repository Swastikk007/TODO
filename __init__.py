from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from app.model import Task  # Adjust the import path as needed
from app import db  # Adjust the import path as needed

def check_pending_tasks():
    now = datetime.now()
    pending_tasks = Task.query.filter_by(status='pending').all()
    for task in pending_tasks:
        if task.deadline and task.deadline < now:
            if not task.last_notified or (now - task.last_notified).total_seconds() > 3600:
                print(f" Notification: Task '{task.name}' is still pending!")
                # you can send email here or flag it in DB
                task.last_notified = now
    db.session.commit()

scheduler = BackgroundScheduler()
scheduler.add_job(func=check_pending_tasks, trigger="interval", hours=1)
scheduler.start()
