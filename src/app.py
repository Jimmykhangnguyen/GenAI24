from flask import Flask, render_template, request

from util import get_charities, graphing

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        have_charity = request.form['have_charity']
        return render_template('q2.html', have_charity=have_charity)
    

@app.route('/q2', methods=['GET', 'POST'])
def q2():
    if request.method == 'GET':
        return render_template('q2.html')
    else:
        charity_name = request.form['charity_name']
        
        return render_template('q2.html', charity_name=charity_name)

@app.route('/charity_info', methods=['GET', 'POST'])
def charity_info():
    if request.method == 'GET':
        return render_template('charity_info.html')
    else:
        charity_name = request.form['charity_name']
        # need to get other info from database/API
        return render_template('charity_info.html', charity_name=charity_name)


@app.route('/search_charities', methods=['GET', 'POST'])
def search_charities():
    if request.method == 'GET':
        return render_template('search_charities.html')
    charity_type = request.form['charities']
    charity_location = request.form['locations']

    charities = get_charities(charity_location, charity_type)
    filenames = graphing(charities)
    listview = []
    for name, info in charities.items():
        dict_ = info['detail']
        dict_['Name'] = name
        dict_['Image'] = filenames[name]
        listview.append(dict_)

    return render_template(
        'search_charities.html',
        charity=[charity_type, charity_location],
        charities=listview,
        combined_image=filenames['combined']
    )


if __name__ == '__main__':
    app.run(debug=True)