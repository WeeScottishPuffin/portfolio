import flask,json,os,random

CAPTURELINK = os.getenv("CLINK")

app = flask.Flask(__name__)

f = open("./static/projects.json","r")
plist = json.load(f)
f.close()

f = open("./static/records.json","r")
rlist = json.load(f)
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

@app.route('/project/portfolio')
def portfolio():
  global plist
  return flask.render_template("portfolio.html",plist=plist)

@app.route('/coolour')
def randomColour():
  return flask.render_template_string('''<html style="width:100vw;height:100vh;overflow:hidden;"><head><title>random colour</title></head><body style="background-color:rgb(%s, %s, %s)"></body></html>'''%(random.SystemRandom().randint(0,255),random.SystemRandom().randint(0,255),random.SystemRandom().randint(0,255)))

#DISCORD VERIFY
@app.route('/.well-known/discord')
def discord():
  return "dh=6219b96f5d5f02c814e2f1ed7163995bbe3ff76f"

@app.route('/notes')
def notes():
  return flask.render_template("records.html",records=rlist)
  
app.run(host='0.0.0.0', port=81)