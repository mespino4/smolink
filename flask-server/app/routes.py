from flask import Flask, jsonify, request, redirect
from models import Urls, db
import random
import string

app = Flask(__name__)

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters

@app.route('/shorten', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        try:
            data = request.get_json()
            url_received = data.get("nm")
            
            found_url = Urls.query.filter_by(long=url_received).first()

            if found_url:
                return jsonify({"short_url": found_url.short})
            else:
                short_url = shorten_url()
                new_url = Urls(url_received, short_url)
                db.session.add(new_url)
                db.session.commit()
                return jsonify({"short_url": short_url})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return "Invalid request"

@app.route('/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return jsonify({"error": "Url doesn't exist"})
