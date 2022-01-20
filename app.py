from flask import Flask, render_template, redirect
import scrape_mars
import pymongo
from flask_pymongo import PyMongo

# Create an instance of our Flask app.
app = Flask(__name__)


# conn = 'mongodb://localhost:27017'

# # Pass connection to the pymongo instance.
# client = pymongo.MongoClient(conn)

# # Connect to a database. Will create one if not already available.
# db = client.mars_db


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Set route
@app.route('/')
def index():
    #mars = mongo.db.mars.find_one()
    return render_template("index.html")

@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    # mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)