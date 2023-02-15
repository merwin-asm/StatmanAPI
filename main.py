"""
STATMAN API

By ~ Darkmash
"""

from flask import Flask, request
import requests as r
import logging
import time

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

WORKERS = {}


@app.route('/')
def main_func_():
  print("PING__UPTIME")
  return """
   <meta
      property="og:image"
      content="https://cdn.discordapp.com/attachments/1023460179087470663/1062001193733337158/image.png"
    />
    <meta
      name="description"
      content="An API for status related activities in Discord."
    />
    <meta name="keywords" content="discord, status , statman ,darkmash , tools , startup , coders" />
    <link
      rel="icon"
      type="image/png"
      href="https://cdn.discordapp.com/attachments/1023460179087470663/1062001193733337158/image.png"
    />
        <title>STATMAN API ~ Darkmash</title>

  ######## DARKMASH ~ STATMAN API ~ V.1.0.0 ###################<br>
  To use the service [GET - method] ,<br>
      /service/wbw/
      {txt} - > word by word (txt should be sep with ~~~ for each break)<br> 
      /service/ca/{txt}  - > cascading animation <br> 
      /service/l/{type}   - > loading <br> 
      /service/lt/{type}/{txt}  - > loading + text <br> 
      /service/stop - > Stop the users processes <br>
      
        &nbsp &nbsp <type> Should be 0 or 1.. <br>
      
      With headers ~ <br>
      &nbsp &nbsp token:token of discord<br> 
  ##############################################################
  """


@app.route('/service/stop', methods=['GET'])
def stop():
  token = request.headers.get("token")
  try:
    WORKERS[token] = False
    return "Done"
  except:
    return "No user found"


@app.route('/service/wbw/<txt>', methods=['GET'])
def wbw(txt):
  headers = {
    "authorization": request.headers.get("token"),
    "user-agent": request.headers.get("user-agent")
  }
  payload = {"custom_status": {"text": ""}}
  url = 'https://discord.com/api/v9/users/@me/settings'

  a = r.patch(url, headers=headers, json=payload)
  if a.status_code == 401:
    return "Invalid Token"
  stats_inp = txt.split("~~~")
  WORKERS.setdefault(request.headers.get("token"), True)
  while WORKERS[request.headers.get("token")]:
    for status in stats_inp:
      payload = {"custom_status": {"text": status}}
      a = r.patch(url, headers=headers, json=payload)
      time.sleep(1)
    time.sleep(1.5)

  del WORKERS[request.headers.get("token")]
  return "ENDED"


@app.route('/service/ca/<txt>', methods=['GET'])
def ca(txt):
  headers = {
    "authorization": request.headers.get("token"),
    "user-agent": request.headers.get("user-agent")
  }
  payload = {"custom_status": {"text": ""}}
  url = 'https://discord.com/api/v9/users/@me/settings'

  a = r.patch(url, headers=headers, json=payload)
  if a.status_code == 401:
    return "Invalid Token"
  status = txt
  while True:
    a_ = ""
    for s in status:
      a_ = a_ + s
      payload = {"custom_status": {"text": a_}}
      a = r.patch(url, headers=headers, json=payload)
      time.sleep(0.1)
    a_ = ""
    time.sleep(1)


@app.route('/service/l/<type>', methods=['GET'])
def l(type):
  headers = {
    "authorization": request.headers.get("token"),
    "user-agent": request.headers.get("user-agent")
  }
  payload = {"custom_status": {"text": ""}}
  url = 'https://discord.com/api/v9/users/@me/settings'

  a = r.patch(url, headers=headers, json=payload)
  if a.status_code == 401:
    return "Invalid Token"
  www = type
  if www == "0":
    status = "|" * 10
    l = 10
  else:
    status = "❚" * 5
    l = 5
  while True:
    a_ = ""
    ad = round(100 / l)
    p = 0
    for s in status:
      p += ad
      if p > 100:
        p = 0

      a_ = a_ + s
      sp = ""

      payload = {"custom_status": {"text": a_ + f" {sp}{p}%"}}
      a = r.patch(url, headers=headers, json=payload)
      time.sleep(0.25)
    a_ = ""
    time.sleep(3)


@app.route('/service/lt/<type>/<txt>', methods=['GET'])
def lt(type, txt):
  headers = {
    "authorization": request.headers.get("token"),
    "user-agent": request.headers.get("user-agent")
  }
  payload = {"custom_status": {"text": ""}}
  url = 'https://discord.com/api/v9/users/@me/settings'

  a = r.patch(url, headers=headers, json=payload)
  if a.status_code == 401:
    return "Invalid Token"
  status_ = txt
  www = type
  if www == "0":
    status = "|" * 10
    l = 10
  else:
    status = "❚" * 5
    l = 5
  while True:
    a_ = ""
    ad = round(100 / l)
    p = 0
    for s in status:
      p += ad
      if p > 100:
        p = 0

      a_ = a_ + s
      sp = ""

      payload = {"custom_status": {"text": a_ + f" {sp}{p}%"}}
      a = r.patch(url, headers=headers, json=payload)
      time.sleep(0.25)
    a_ = ""

    payload = {"custom_status": {"text": status_}}
    a = r.patch(url, headers=headers, json=payload)
    time.sleep(2)


app.run(host="0.0.0.0", port=8080)
