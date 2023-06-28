from os import path
from flask import Blueprint, render_template

views_dir = path.abspath("./src/views")
router = Blueprint("router", __name__, template_folder=views_dir)


@router.route("/")
def index():
    return render_template("home.html")
