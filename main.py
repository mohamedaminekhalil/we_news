from flask import Flask, render_template, jsonify
from databse_functions import *
from api import generate_articles
from datetime import date

CATEGORIES_LIST = ("business", "entertainment", "general", "health", "science", "sports", "technology")
app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home_page.html", title="we news", custom_css="home_custom")


# Post request to update read later status of an article in database
@app.route("/toggle_later/<int:article_id>", methods=["POST"])
def toggle_later(article_id):
    toggle_later_status(article_id)
    return jsonify({"success": True})


# Post request to update saved status of an article in database
@app.route("/toggle_saved/<int:article_id>", methods=["POST"])
def toggle_saved(article_id):
    toggle_saved_status(article_id)
    return jsonify({"success": True})


# Routing for today page and retrieval of the trending today articles
@app.route("/today")
def today():
    data_to_store = generate_articles(CATEGORIES_LIST)
    insert_data(data_to_store)
    data = retrieve_data_by_date(date.today())
    return render_template("news.html", title="Today's news", custom_css="news_custom",
                           custom_js="news", categories=CATEGORIES_LIST, articles=data)


@app.route("/later")
def read_later():
    data = retrieve_data_by_later()
    return render_template("news.html", title="Read later", custom_css="news_custom",
                           custom_js="news", categories=CATEGORIES_LIST, articles=data)


@app.route("/saved")
def saved():
    data = retrieve_data_by_saved()
    return render_template("news.html", title="Saved", custom_css="news_custom",
                           custom_js="news", categories=CATEGORIES_LIST, articles=data)


@app.route("/archive")
def archive():
    dates = get_unique_values()
    return render_template("archive.html", title="Archive", dates=dates, custom_css="archive_custom")


@app.route('/<string:d>')
def date_page(d):
    data = retrieve_data_by_date(d)
    if str(d) == str(date.today()):
        return today()
    else:
        return render_template('news.html', title=d, custom_css="news_custom",
                               custom_js="news", categories=CATEGORIES_LIST, articles=data)


app.run(debug=True, host="0.0.0.0", port=2000)
