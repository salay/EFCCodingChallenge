# EFCCodingChallenge

Optimizing a fleet of trucks that are delivering flour! Bake all the cakes!

It's a work in progress:

I'm using Python, Flask, Peewee, Postgres, and may add JS or a call to the google maps API
#### In order to create the database, I ran the following commands in the terminal: 

$ CREATE DATABASE flourdeliveries;  
$ CREATE TABLE location (id SERIAL PRIMARY KEY, name VARCHAR(200), address VARCHAR(255));   
$ CREATE TABLE truck (id SERIAL PRIMARY KEY, region VARCHAR(255), flourCapacity INTEGER;  
$ CREATE TABLE deliveries (id SERIAL PRIMARY KEY, flourAmt INTEGER, deliveryDatetime TIMESTAMP, truck_id INTEGER REFERENCES truck(id), location_id INTEGER REFERENCES location(id));

In order to run the app use the following commands:

1) install virtual env  
$ pip3 install virtualenv    
$ virtualenv .env -p python3   
$ source .env/bin/activate    

2) install dependencies . 
$ pip3 install flask #installs flask, the python microframework   
$ pip3 install peewee #installs peewee ORM   
$ pip3 install psycopg2-binary #needed to run postgresql db
  
3) try running app . 
$ python3 app.py

