from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import datetime
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('admin', __name__)

@bp.route('/admin')
def admin():
    return render_template('admin/admin.html')
