from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/vowels')
def animals_form():
	return render_template('blank_template.html')

@app.route('/vowel-result')
def animals_result():
	if request.method == 'GET':
		result = request.args
		name = str.lower(result.get('name'))
		vowels = ['a', 'e','i','o','u']
		total = 0
		for c in name:
			if c in vowels:
				total +=1
		
		return render_template('vowels_result.html', t = total)

if __name__=='__main__':
	app.run(debug=True)
