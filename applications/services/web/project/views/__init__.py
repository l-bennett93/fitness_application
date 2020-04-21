import os
from werkzeug.utils import secure_filename
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for,
    Blueprint
)
from project import app

basic_blueprint = Blueprint(__name__, "basic_blueprint")


@basic_blueprint.route("/")
def hello_world():
    return jsonify(hello="world")


@basic_blueprint.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@basic_blueprint.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)


@basic_blueprint.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    return f"""
    <!doctype html>
    <title>upload new File</title>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file><input type=submit value=Upload>
    </form>
    """
