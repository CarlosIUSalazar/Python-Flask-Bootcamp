from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, 
                    RadioField, SelectField, TextField, 
                    TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):

    breed = StringField('What breed are you?', validators=[DataRequired()])
    neuter = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood:', 
                        choices=[('mood_one','Happy'),('mood_two','excited')])
    food_choice = SelectField(u'Pick your favorite food:',choices=[('chi','Chicken'),('bf','Beef'),
                                                                    ('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():   #if form is valid on submission (verifies that validators were successful)
        session['breed'] = form.breed.data   #breed is a new key in the session dictionary. form.breed.data is the info within the class that we specified.
        session['neuter'] = form.neuter.data
        session['mood'] = form.neuter.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))    #this return is only accessed after the form is submitted

    return render_template('index.html', form=form)    #This return is displayed first as index.html


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)