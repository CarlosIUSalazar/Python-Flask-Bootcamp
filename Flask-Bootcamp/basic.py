from flask import Flask

app = Flask(__name__)   #creating an application object as an instance of the class Flask. The name variable is a predefined python variable which is then set to the nane of the module and then used.  Flask is able to use the location of the module that we passed in as a starting point when needs to load another resources of files.

@app.route('/')     #Directly link the pages to the route / (home page of domain)
def index():        #Defines a page (index) and returns a string <h1>
    return '<h1>Hello Pyppy!<h1>'

@app.route('/information')
def info():
    return "<h1>Puppies are cute!<h1>"

# @app.route('/puppy/<name>')
# def puppy(name):
#     #return "<h1>Upper case: {}</h1>".format(name.upper())
#     return "100th letter: {}".format(name[100])

@app.route('/puppy_latin/<name>')
def puppy(name):
    origName = name
    if origName[-1] == 'y':
        origName = origName[:-1] + 'iful'
    else:
        origName = origName + 'y'
    return "Hi {}! Your puppylatin name is {}.".format(name,origName)

if __name__ == '__main__':
    app.run(debug=True)
