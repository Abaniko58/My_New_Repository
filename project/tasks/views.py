import datetime
from functools import wraps
from flask import flash, redirect, render_template, \
    request, session, url_for, Blueprint

from .forms import AddInstForm, SubscrUserForm
from project import db
from project.models import Fan, User, Subscr


################
#### config ####
################

tasks_blueprint = Blueprint('tasks', __name__, template_folder='templates', static_folder='static')


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


#def open_tasks():
#    return Fan.query.filter_by(user_id=session['name'])



################
#### routes ####
################

@tasks_blueprint.route('/tasks/')
@login_required
def tasks():
    open_subscrs = db.session.query(Subscr).filter_by(user_id=session['user_id'])
    open_tasks = Fan.query.filter_by(user_id=session['user_id'])
    return render_template(
        'tasks_users.html',
        open_tasks = open_tasks,
        open_subscrs = open_subscrs,
        username = session['name']
    )

@tasks_blueprint.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    error = None

    form = AddInstForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            addtask = Fan(
                form.date_inst.data,
                form.sat_net.data,
                form.positions.data,
                form.convertors.data,
                form.resivers.data,
                form.add_net.data,
                form.add_terr.data,
                form.access.data,
                form.user_id.data
            )
            db.session.add(addtask)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
            return redirect(url_for('tasks.instal'))
        return redirect(url_for('tasks.add'))
    return render_template(
        'addinst.html',
        form=form)


@tasks_blueprint.route('/info/<int:user_id>/')
@login_required
def info(user_id):
    new_id = user_id
    open_users = db.session.query(User).filter_by(id=new_id)
    open_insts = db.session.query(Fan).filter_by(user_id=new_id)
    open_subscrs = db.session.query(Subscr).filter_by(user_id=new_id)
    flash("You may search user's data")
    return render_template('info.html', open_users=open_users, open_insts=open_insts, open_subscrs=open_subscrs)


@tasks_blueprint.route('/add_subscr/', methods=['GET', 'POST'])
@login_required
def add_subscr():
    error = None
    form = SubscrUserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            addtask = Subscr(
                form.date_subscr.data,
                form.provider.data,
                form.class_subscr.data,
                form.date_end_subscr.data,
                form.costs.data,
                form.balance.data,
                form.user_id.data
            )
            db.session.add(addtask)
            db.session.commit()
            flash('New subscription was successfully added. Thanks.')
            return redirect(url_for('tasks.tasks'))
        return redirect(url_for('tasks.add_subscr'))
    return render_template(
        'add_subscr.html',
        form=form)

@tasks_blueprint.route('/instal/', methods=['GET', 'POST'])
@login_required
def instal():
    error = None
    open_instals = Fan.query.all()
    #    open_users = db.session.query(User).all()
    if request.method == 'POST':
        look = request.form.get('look')
        val1 = int(request.form.get('selected_value'))
        print(look, val1)
        if val1 == 1:
            # name
            open_instals = db.session.query(Fan).filter_by(sat_net=int(look))
        elif val1 == 2:
            # adress
            open_instals = Fan.query.filter(Fan.resivers.contains(look)).all()
            # id
        elif val1 == 3:
            open_instals = db.session.query(Fan).filter_by(date_inst=look)
        elif val1 == 4:
            open_instals = Fan.query.filter_by(user_id=int(look))
        else:
            open_instals = Fan.query.all()

    return render_template('instal_users.html', open_insts=open_instals, error=error)

@tasks_blueprint.route('/subscrs/', methods=['GET', 'POST'])
@login_required
def subscrs():
    error = None
#    open_instals = Fan.query.all()
    open_subscrs = db.session.query(Subscr).all()
    if request.method == 'POST':
        look = request.form.get('look')
        val1 = int(request.form.get('selected_value'))
        if val1 == 1:
            # prov
            open_subscrs = Subscr.query.filter(Subscr.provider.contains(look)).all()
        elif val1 == 2:
            # prov
            open_subscrs = Subscr.query.filter(Subscr.class_subscr.contains(look)).all()
        elif val1 == 3:
            # adress
            open_subscrs = db.session.query(Subscr).filter_by(date_subscr=look)
            # id
        elif val1 == 4:
            open_subscrs = db.session.query(Subscr).filter_by(date_end_subscr=look)
        else:
            open_subscrs = Subscr.query.all()
    return render_template('subscrs.html', open_subscrs=open_subscrs, error=error)
