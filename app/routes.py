
from app import app
from flask import render_template

@app.route('/')
def real_home():
    bands = ['Manchester Orchestra','Vance Joy','All Get Out','Matt Maeson','City & Colour']
    return render_template('index.html', bands = bands)

@app.route('/fav_5')
def real_fav():
    bands = ['Manchester Orchestra','Vance Joy','All Get Out','Matt Maeson','City & Colour']
    return render_template('fav_five.html', bands = bands)


