from flask import Flask
from flask import render_template
from flask import request

from mycoder import incode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coder')
def coder():

    try:
        ans = incode(request.args['street'], request.args['number'])
    except Exception as e:
        return e.args[0], 400

    if 'pretty' in request.args and request.args['pretty'] == 'true':
        return render_template('ans.html', lat=ans[0], lon=ans[1], address=ans[2])
    else:
        return str(ans[0]) + ' ' + str(ans[1])
