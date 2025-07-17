from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from app import db
from app.model import Task
from datetime import datetime, timedelta
from app.routes.auth import auth_bp

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/viewtasks', methods=['GET'])
def viewtasks():
    if 'user' not in session:
        flash('you need to login first', 'warning')
        return redirect(url_for('auth.login')  )
    
    tasks = Task.query.all()
    return render_template('task.html', tasks=tasks)

@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if 'user'not in session:
        return redirect(url_for('auth.login'))
    
    tittle = request.form.get('tittle')
    dead_line= request.form.get('deadline')
    if tittle and dead_line:
        new_task = Task(name=tittle, status = 'pending', deadline= dead_line)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', 'success')
        return redirect(url_for('task.viewtasks'))

@tasks_bp.route('/update/<int:task_id',methods = ['POST'])
def update_status(task_id):
    task = Task.query.get(task_id)
    if task:
        task.status = 'done'
        db.session.commit()
        flash('Task status updated successfully', 'success')
        return redirect(url_for('task.viewtasks'))


@tasks_bp.route('/extend/<int:task_id>', methods = ['POST'])
def update_deadline(task_id):
    new_deadline = request.form['new_deadline']
    task = Task.query.get(task_id)
    task.deadline = datetime.strptime(new_deadline, '%Y-%m-%dT%H:%M')
    task.last_notified = None  # reset notification
    db.session.commit() 
    return redirect(url_for('task.viewtasks'))
   
@tasks_bp.route('/delete/<int:task_id>',methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully', 'success')
    return redirect(url_for('task.viewtasks'))

@tasks_bp.route('/delete_all', methods=['POST'])
def delete_all_tasks():
    Task.query.delete()
    db.session.commit()
    flash('All tasks deleted sucessfully', 'success') 

@tasks_bp.route('/isempty', methods = ['GET'])
def is_empty():
    task = Task.query.all()
    if not task:
        flash('No tasks available', 'info')
        return redirect(url_for('task.add_task'))
