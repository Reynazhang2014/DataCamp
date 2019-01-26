import numpy as np
import pandas as pd
import sqlalchemy
import datetime as dt
import dateutil.parser as dp
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Station = Base.classes.station
Measurement = Base.classes.measurement
session = Session(engine)

#define start date ane end date of trip
start_day = '2017-01-01'
end_day = '2017-01-15'

# def calc_temps(start_date, end_date):
#     min,avg,max = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
#         filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()[0]
#     temp_info = {"Min Temparature": min,"Avg Temperature": avg,"Max Temperature": max}
#     return temp_info
# print(calc_temps("2017-01-01","2017-01-15"))

app = Flask(__name__)
@app.route("/")
def Welcome():
    return "Welcome to Hawaii history database!"
@app.route("/api/v1.0/precipitation")
def Precipitation():
    prcp = session.query(Measurement.date,Measurement.prcp).all()
    return jsonify(dict(prcp))

@app.route("/api/v1.0/stations")
def GetStation():
    station = session.query(Station.station,Station.name).distinct().all()
    return jsonify(dict(station))

@app.route("/api/v1.0/tobs")
def GetLastYearTemp():
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    one_year_ago = dp.parse(*last_day) - dt.timedelta(days = 365)
    one_year_tobs = pd.read_sql(session.query(Measurement.date,Measurement.tobs).filter(func.Date(Measurement.date) >= one_year_ago).statement,session.bind)
    one_year_tobs.set_index('date',inplace= True)
    return jsonify(one_year_tobs.to_dict())

@app.route("/api/v1.0/<start>")
def GetMinMaxAvgTem(start):
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    minn,avgg,maxx = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(func.Date(Measurement.date) >= start).filter(func.Date(Measurement.date) <= last_day).all()[0]
    temp_info = {"Min Temparature": minn,"Avg Temperature": avgg,"Max Temperature": maxx}
    return jsonify(temp_info)

@app.route("/api/v1.0/<start>/<end>")
def GetMinMaxAvgTemTwo(start,end):
    minn,avgg,maxx = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(func.Date(Measurement.date) >= start).filter(func.Date(Measurement.date) <= end).all()[0]
    temp_info = {"Min Temparature": minn,"Avg Temperature": avgg,"Max Temperature": maxx}
    return jsonify(temp_info)


if __name__ == '__main__':
    app.run(debug=True)
