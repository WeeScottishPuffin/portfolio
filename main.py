import flask
import json
import os

CAPTURELINK = os.getenv("CLINK")

app = flask.Flask(__name__)

f = open("./static/projects.json","r")
plist = json.load(f)
f.close()

@app.route('/')
def index():
  global plist
  l = dict(sorted(plist.items()))
  return flask.render_template("index.html",projects=l,captureLink=CAPTURELINK)

@app.route('/project/<pname>')
def project(pname):
  global plist
  return flask.render_template("project.html",project=plist[pname])

app.run(host='0.0.0.0', port=81)