#################
#### imports ####
#################

from functools import wraps
from flask import flash, redirect, render_template, \
    request, session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError

from .forms import RegisterForm, LoginForm, SearchForm
from project import db, bcrypt
from project.models import User


################
#### config ####
################

users_blueprint = Blueprint('users', __name__, template_folder='templates', static_folder='static')


##########################
#### helper functions ####
##########################


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

#def open_users():
#    return User.query.all()
################
#### routes ####
################

@users_blueprint.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('user_fio', None)
    session.pop('adress', None)
    session.pop('phone', None)
    session.pop('role', None)
    session.pop('name', None)
    flash('Goodbye!')
    return redirect(url_for('start.index'))


@users_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
#    flash('Please login.')
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                session['logged_in'] = True
                session['user_id'] = user.id
                session['user_fio'] = user.fio
                session['adress'] = user.adress
                session['phone'] = user.phone
                session['name'] = user.name
                session['role'] = user.role
#                flash('Welcome!')
                if user.role == 'admin':
                    return redirect(url_for('users.admin'))
                return redirect(url_for('tasks.tasks'))
            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                form.fio.data,
                form.adress.data,
                form.phone.data,
                form.name.data,
                form.email.data,
                bcrypt.generate_password_hash(form.password.data)
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering. Please login.')
                return redirect(url_for('users.login'))
            except IntegrityError:
                error = 'That username and/or email already exist.'
#    if session['role'] == 'admin':
    return render_template('register_n.html', form=form, error=error)
#    else:
#        return render_template('register.html', form=form, error=error)
#    return render_template('register.html', form=form, error=error)


@users_blueprint.route('/admin/', methods=['GET', 'POST'])
@login_required
def admin():
#    flash('Hello, Admin!')
    error = None
    open_users = User.query.all()
#    open_users = db.session.query(User).all()
    if request.method == 'POST':
        look = request.form.get('look')
        val1 = int(request.form.get('selected_value'))
        print(look, val1)
        if val1 == 1:
            #name
            open_users = User.query.filter(User.fio.contains(look)).all()
        elif val1 == 2:
            #adress
            open_users = User.query.filter(User.adress.contains(look)).all()
            #id
        elif val1 ==3:
            open_users = db.session.query(User).filter_by(name=look)
        elif val1 ==4:
            open_users = User.query.filter_by(id=int(look))
        else:
            open_users = User.query.all()

    return render_template('admin_user.html', open_users=open_users, error=error, username=session['name'])


@users_blueprint.route('/delete/<int:user_id>/')
@login_required
def delete_entry(user_id):
    new_id = user_id
    user = db.session.query(User).filter_by(id=new_id)
    if  session['role'] == "admin":
        user.delete()
        db.session.commit()
        flash('The user was deleted. Why not add a new one?')
        return redirect(url_for('users.admin'))
    else:
        flash("It's impossible...")


@users_blueprint.route('/edit_user/<int:user_id>/', methods=['GET', 'POST'])
def edit_user(user_id):
    new_id = user_id
    error = None
    form = RegisterForm(request.form)
    open_user = User.query.filter_by(id=new_id)
    if request.method == 'POST':
        if form.validate_on_submit():
            ed_user = User(
                form.fio.data,
                form.adress.data,
                form.phone.data,
                form.name.data,
                form.email.data,
                bcrypt.generate_password_hash(form.password.data)
            )
            try:
                db.session.update(ed_user)
                db.session.commit()
                flash('Thanks for registering. Please login.')
                return redirect(url_for('users.login'))
            except IntegrityError:
                error = 'That username and/or email already exist.'
#    if session['role'] == 'admin':
    return render_template('edit_user.html', form=form, error=error, open_user=open_user)