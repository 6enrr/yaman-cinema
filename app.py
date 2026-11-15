from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
API_KEY = "0eacef06dfde019f78049894361ee9fb"

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q")
    movie_id = request.args.get("watch")

    movies = []
    if query:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}&language=ar"
        title_header = f"نتائج البحث عن: {query}"
        response = requests.get(url).json()
        movies = response.get("results", [])
    else:
        title_header = "🔥 مكتبة يمان سينما الشاملة (أفلام لا تنتهي)"
        for page in range(1, 5):
            url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ar&page={page}"
            response = requests.get(url).json()
            movies.extend(response.get("results", []))

    return render_template("index.html", movies=movies, title_header=title_header, watch_id=movie_id)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
