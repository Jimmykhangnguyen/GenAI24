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
        return render_template('q2.html', have_charity=have_charity)


if __name__ == '__main__':
    app.run(debug=True)