from flask import Flask,session,render_template,request
import os
from swimclub import process_swim_data,FOLDER
app = Flask(__name__)
app.secret_key ="You'll never guess"

@app.get("/")
def index():
    return render_template(
        "index.html",
        title = "Welcome to Swim club System",
        )

def populate_data():
    if "swimmers" not in session:
         session["swimmers"] = {}
         filenames = os.listdir(FOLDER)
         filenames.remove(".DS_Store")

         for file in filenames:
          name =process_swim_data(file)["name"]
          if name not in session["swimmers"]:
            session["swimmers"][name] = []
            session["swimmers"][name].append(file)

@app.get("/swimmers")
def display_swimmers():
    populate_data()
    return render_template(
        "select.html",
        title="Select a Swimmer",
        url="/showfiles",
        select_id="swimmer",
        names=sorted(session["swimmers"]),
        )


@app.post("/showfiles")
def get_swimmers_files():
    populate_data()
    name = request.form["swimmer"]
    return render_template(
        "select.html",
        title="Select swimmer's file",
        url="/showbarchart",
        select_id="file",
        names=session["swimmers"][name],
        )


if __name__ == "__main__":
    app.run(debug = True)