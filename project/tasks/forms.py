from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired


class SubscrUserForm(Form):
    id_subscr = IntegerField()
    date_subscr =   DateField('Date Subscr (dd/mm/yyyy)',  format='%d/%m/%Y')
    provider = StringField('Provider')
    class_subscr = StringField('Class subscr')
    date_end_subscr = DateField('Date Subscr (dd/mm/yyyy)',  format='%d/%m/%Y')
    costs = StringField('Price subscr')
    balance = StringField('Balance')
    user_id = IntegerField()


class AddInstForm(Form):
    id_inst = IntegerField()
    date_inst = DateField(
        'Date Due (dd/mm/yyyy)',
        validators=[DataRequired()], format='%d/%m/%Y'
        )
    sat_net = IntegerField('Sat-Net', validators=[DataRequired()])
    positions = StringField('Positions', validators=[DataRequired()])
    convertors = StringField('Convertors', validators=[DataRequired()])
    resivers =  StringField('Recivers', validators=[DataRequired()])
    add_net = StringField('Add_net', validators=[DataRequired()])
    add_terr = StringField('Add_terr', validators=[DataRequired()])
    access = StringField('Task Name', validators=[DataRequired()])
    user_id = IntegerField()
