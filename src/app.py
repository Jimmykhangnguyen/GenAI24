from flask import Flask, render_template, request

app = Flask(__name__)

charities = [
    {
        "Name": "Canadian Cancer Society",
        "Mission": "The Canadian Cancer Society is a national, community-based organization of volunteers whose mission is to eradicate cancer and enhance the quality of life of people living with cancer.",  
        "Publicperceptionsonthescalefrom1to10": 8,  
        "Impact": "The Canadian Cancer Society has a significant impact on the lives of Canadians affected by cancer. The organization provides a wide range of programs and services, including cancer research, patient support, and public education.",  
        "FundraisingTechnique": "The Canadian Cancer Society raises funds through a variety of methods, including donations, special events, and corporate partnerships.",  
        "Financialtransparency": 9
    },
    {
        'name': 'Charity 2',
        'type': 'Type 2',
        'info': 'Info 2',
    },
    {  
        'name': 'Charity 3',
        'type': 'Type 3',
        'info': 'Location 3',
    },
    {
        'name': 'Charity 4',
        'type': 'Type 1',
        'info': 'Location 1',
    },
    {
        'name': 'Charity 5',
        'type': 'Type 2',
        'info': 'Location 2',
    },
    {  
        'name': 'Charity 6',
        'type': 'Type 3',
        'info': 'Location 3',
    }
]

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
    else:
        charity_type = request.form['charities']
        charity_location = request.form['locations']

        return render_template('search_charities.html', charity=[charity_type, charity_location], charities=charities)


if __name__ == '__main__':
    app.run(debug=True)