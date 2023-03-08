from flask import ( Blueprint, render_template, request, redirect)

bp = Blueprint("fact", __name__, url_prefix="/facts")

@bp.route("/")
def index():
    return render_template("facts/index.html")

@bp.route("/new", methods=("GET", "POST"))
def new():
    # if request.method == "GET"

    if request.method == "POST":
        print("Posted data")
        submitter = request.form["submitter"]
        fact = request.form["fact"]

        print(f"Lorem ispum: {fact}, by {submitter}")

        return redirect("/facts")
    
    return render_template("facts/new.html")