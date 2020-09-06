from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

#configure security key
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    breed = StringField("What Breed are you?")
    submit = SubmitField('Submit')  #'submit' is what the button says

@app.route('/',methods=['GET','POST'])
def index():

    breed = False
    form = InfoForm()  #Create instance of form
    if form.validate_on_submit():  #If form is valid on submission
        breed = form.breed.data #form(is the form) breed is from class InfoForm breed, and data is what was input into breed.
        form.breed.data = ''   #reset this value so the field is empty again
    return render_template('index.html', form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)
    

