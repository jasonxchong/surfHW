from flask import Flask, jsonify

import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import numpy as np
from datetime import datetime

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station
session=Session(engine)


app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"API Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
	results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date.between('2016-09-01', '2017-08-31')).all()

	data_dict = list(np.ravel(results))
	results.___dict___
	#Create a dictionary using 'date' as the key and 'prcp' as the value.
	year_prcp = []
	for results in results:
		row = {}
		row[Measurement.date] = row[Measurement.prcp]
		year_prcp.append(row)

	return jsonify(data_dict)


@app.route("/api/v1.0/stations")
def stations():
	results = session.query(Station.station).all()

	all_stations = list(np.ravel(results))

	return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temperature():
	year_tobs = []
	results = session.query(Measurement.tobs).filter(Measurement.date.between('2016-09-01', '2017-08-31')).all()

	year_tobs = list(np.ravel(results))

	return jsonify(year_tobs)


if __name__ == '__main__':
    app.run(debug=True)
