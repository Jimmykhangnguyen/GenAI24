from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        have_charity = request.form['have_charity']
        return render_template('question.html', have_charity=have_charity)

@app.route('/charity_info', methods=['GET', 'POST'])
def charity_info():
    if request.method == 'GET':
        return render_template('charity_info.html')
    else:
        charity_name = request.form['charity_name']
        return render_template('charity_info.html', charity_name=charity_name)


@app.route('/search_charities', methods=['GET', 'POST'])
def search_charities():
    if request.method == 'GET':
        return render_template('search_charities.html')
    else:
        charity_type = request.form['charities']
        charity_location = request.form['locations']

        charity = [charity_type, charity_location]
        return render_template('search_charities.html', charity=charity)


if __name__ == '__main__':
    app.run(debug=True)