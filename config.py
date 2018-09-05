from flask import Flask
from flask import render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
#from flask.ext.wtf.csrf import CsrfProtect


database_url = 'postgresql://postgres:3300347@localhost:5432/gis_papers'

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['WTF_CSRF_ENABLED'] = False

db = SQLAlchemy(app)

csrf = CsrfProtect(app)

@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            pass

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = some_random_string()
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token    
