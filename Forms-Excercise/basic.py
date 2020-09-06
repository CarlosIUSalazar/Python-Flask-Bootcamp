from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report.html')
def report():
    userName = request.args.get('username')

    haveUpper = False
    haveLower = False
    num_end = False

    haveLower = any(c.islower() for c in userName)  #
    haveUpper = any(c.isupper() for c in userName)
    num_end = userName[-1].isdigit()

    report = haveLower and haveUpper and num_end == True

    return render_template('report.html', report=report, lower=haveLower, upper=haveUpper, num_end=num_end)

if __name__ == '__main__':
    app.run(debug=True)


    # haveUpper = False
    # haveLower = False
    # reason1 = ''
    # reason2 = ''
    # reason3 = ''

    # if userName[-1].isnumeric() == False:
    #     reason3 = 'The last character is not a number'

    # for char in userName:
    #     if char.isupper():
    #         haveUpper = True

    # for char in userName:
    #     if char.isupper() == False:
    #         haveLower = True

    # if haveUpper == False:
    #     reason1 = 'You did not use an uppercase character.'

    # if haveLower == False:
    #     reason2 = 'You did not use a lowercase character'

    # if reason1 == '' and reason2 == '' and reason3 == '':
    #     allgood = 'Your User Name is Secure'
    #     return render_template('report.html',)
    # else:
    #     return render_template('report.html', reason1=reason1, reason2=reason2, reason3=reason3)
    