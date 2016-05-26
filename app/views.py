from flask import render_template

from app import app



@app.route('/index')


def index():
    user = {'nickname': 'Miguel'}  # fake user
    """function to get travelinformation from google maps/calendar and userinfo"""
    return render_template('index.html',
                           title='Home',
                           location ='beijum',
                           end_location = 'grote markt 1, Groningen',
                           end_time = '14:00',
                           travel_time = '30 minutes',
                           user=user)

if __name__ == '__main__':
    app.run()
