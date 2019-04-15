## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).
import requests
import json
from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True

## Tool functions (e.g. could go in a separate file and be imported for invocation...)
def get_itunes_data(artist_search):
    params = {}
    params["term"] = artist_search
    resp = requests.get('https://itunes.apple.com/search', params = params)
    data = json.loads(resp.text)
    return data
    
## No models in this app -- this one doesn't deal with databases
    
## Route functions
    
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistform')
def artist_form():
    return render_template('artistform.html')

@app.route('/artistinfo') # You would only get to this route -- should only -- by submitting the form found at /artistform
def artist_info():
    if request.method == 'GET': # Just to ensure -- there should not be another case
        result = request.args
        artist_to_search = result.get('artist')
        data = get_itunes_data(artist_to_search)
        return render_template('artist_info.html', objects = data['results'])


if __name__=='__main__':
    app.run(debug=True)
