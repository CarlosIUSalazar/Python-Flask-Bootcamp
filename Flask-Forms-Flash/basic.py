from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kmykey'

class SimpleForm(FlaskForm):

    submit = SubmitField('Click me')

@app.route('/',methods=['GET','POST'])
def index():

    form = SimpleForm()

    if form.validate_on_submit():
        flash('You just clicked the button!') #this causes an object called get_flashed_messages() to be available in index.html
        return redirect(url_for('index')) #We are serving the same page again

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)