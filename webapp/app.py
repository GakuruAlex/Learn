from flask import Flask,session,render_template
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
def display_swimmers()->list:
    populate_data()
    return render_template(
        "select.html",
        names = sorted(session["swimmers"])),
    
@app.get("/files/<swimmer>")
def get_swimmers_files(swimmer):
    populate_data()
    return str(session["swimmers"][swimmer])

if __name__ == "__main__":
    app.run()