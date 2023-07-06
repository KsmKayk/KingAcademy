from os import path
from flask import Blueprint, render_template, redirect, request, url_for, session

views_dir = path.abspath("./src/views")
router = Blueprint("router", __name__, template_folder=views_dir)


@router.route("/")
def index():
    if "signed" in session:
        return render_template(
            "home.html", signed=True, user_email="teste@gmail.com", user_name="John Doe"
        )
    else:
        return render_template("home.html", signed=False)


@router.route("/signout", methods=["POST"])
def signout():
    session.pop("signed", None)
    return redirect(url_for("router.index"))


@router.route("/signin")
def signin():
    session["signed"] = True
    return redirect(url_for("router.index"))
