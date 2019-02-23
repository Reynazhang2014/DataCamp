from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

#mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#conn = 'mongodb://localhost:27017'
#client = pymongo.MongoClient(conn)

#db = client.mars_db

# drop all exising documents (if any)

@app.route("/")
def index():
    mars_data = mongo.db.mars.find_one()
    return render_template("index_Reyna.html", mars_data=mars_data)

@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    data = scrape_mars.scrape()
    mars.update(
        {},
        data,
        upsert=True
    ) 
    return redirect("/", code=302)




if __name__ == "__main__":
    app.run(debug=True)