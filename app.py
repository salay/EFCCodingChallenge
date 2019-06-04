from flask import (
     Flask, g, flash, redirect, render_template, request, session, url_for
)

import models

import datetime
import os

app = Flask(__name__)

DEBUG = True
PORT = 8000
@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

def query_db(query, args=(), one=False):
    cur = g.db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

for user in query_db('select sum (flourAmt) from deliveries where date > dateadd(year,-1,getdate()) group by location order by flourAmt desc'):
    print(deliveries['flourAmt'], 'has the location', deliveries['location'])

@app.route('/', methods=['GET', 'POST'])
def index():
    top_locations_by_weight_past_yr = models.Deliveries.select()
    return render_template("home.html", locationsByWeight=top_locations_by_weight_past_yr)

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)