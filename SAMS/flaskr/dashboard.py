from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import datetime
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
    db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    classes = db.execute(
        'SELECT c.id, student_id, class_id, time, location, attended, late, outside'
        ' FROM class c JOIN user u ON c.student_id = u.id'
        ' WHERE c.student_id = u.id'
        ' ORDER BY class_id DESC'
    ).fetchall()

    return render_template(
        'dashboard/index.html', 
        classes=classes, 
        allowAttend=allowAttend, 
        getNextClass=getNextClass, 
        isStr=isStr,
        )
    
def getNextClass():
    db = get_db()
    cursor = db.cursor()
    classes = cursor.execute
    classes = db.execute(
        'SELECT c.id, student_id, class_id, time, location, attended, late, outside, class_title'
        ' FROM class c JOIN user u ON c.student_id = u.id'
        ' WHERE c.student_id = u.id'
    ).fetchall()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    earliest = None
    passed = None
    for c in classes:
        id, sid, cid, time, location, attended, late, outside, ctitle = c
        if time >= now and (earliest is None or time < earliest['time']):
            earliest = c
        if now > time and (passed is None or time > passed['time']):
            passed = c

    # check if none, and if previous class is within 30 minutes
    nextClass = earliest
    if allowAttend(passed['time']) < 30:
        nextClass = passed
    return nextClass

def allowAttend(classTime):
    difference = (datetime.datetime.now() - datetime.datetime.strptime(classTime, "%Y-%m-%d %H:%M:%S")).total_seconds() / 60
    return difference

@bp.context_processor
def inject_today_date():
    return {'today_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

def isStr(obj):
    return isinstance(obj, str)

@bp.route('/takeAttendance', methods=('GET', 'POST'))
def takeAttendace():
    db = get_db()
    error = None
    classes = db.execute(
        'SELECT c.id, student_id, class_id, time, location, attended, late, outside, class_title'
        ' FROM class c JOIN user u ON c.student_id = u.id'
        ' WHERE c.student_id = u.id'
        ' ORDER BY class_id DESC'
    ).fetchall()
    if request.method == 'POST':
        student = request.form['student']
        lesson = request.form['lesson']
        time = request.form['time']
        print(student, lesson, time)
        try:
            db.execute(
                'UPDATE class SET attended = ?'
                ' WHERE student_id = ? AND class_id = ? AND time = ?',
                (1, student, lesson, time )
            )
            db.commit()
            success = "Attendance marked!"
            flash(success)
            return redirect(url_for('index'))
        except db.IntegrityError:
            error = "Something went wrong."
            flash(error)
    #     username = request.form['username']
    #     password = request.form['password']
    #     db = get_db()
    #     error = None
    #     user = db.execute(
    #         'SELECT * FROM user WHERE username = ?', (username,)
    #     ).fetchone()

    #     if user is None:
    #         error = 'Incorrect username.'
    #     elif not check_password_hash(user['password'], password):
    #         error = 'Incorrect password.'
    #     print(user)

    #     if error is None and username == 'admin':
    #         session.clear()
    #         session['user_id'] = user['id']
    #         return redirect(url_for("admin.admin"))
    #     elif error is None:
    #         session.clear()
    #         session['user_id'] = user['id']
    #         return redirect(url_for('index'))
    #     flash(error)
    return render_template(
        'dashboard/index.html', 
        classes=classes, 
        allowAttend=allowAttend, 
        getNextClass=getNextClass, 
        isStr=isStr,
        )

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('dashboard.index'))

    return render_template('dashboard/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('dashboard.index'))

    return render_template('dashboard/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('dashboard.index'))
