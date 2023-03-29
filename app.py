from flask import Flask, render_template, session, request
from apis import unsplash
from apis import national_parks
import json
from pprint import pprint

app = Flask(__name__)
app.secret_key = 'slfksflk353943049'

@app.route("/", methods=['GET',"POST"])
def home():
    if not session.get('unsplash_images'):
        unsplash_response, error = unsplash.get_image_response()
        session['unsplash_images'] = unsplash.create_image_object_list(unsplash_response) 
        image_list = session['unsplash_images']
    else:
        image_list = session.get('unsplash_images')

    query = request.form.get('search_query')
    if query:
        park_data_response, error = national_parks.get_parks_data(query)
        returned_park_list = national_parks.create_park_objects_list(park_data_response)
    else:
        returned_park_list=None
    return render_template("index.html", image_list=image_list, park_data=returned_park_list)


@app.route("/display_saved_parks", methods=['GET',"POST"])
def bookmarked():
    return render_template("bookmarked.html")


