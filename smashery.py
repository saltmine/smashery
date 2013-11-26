#!/usr/bin/env python
"""Main app file for interacting with the Smashery proxy"""

from flask import Flask
import requests
from config import settings

PORT = 5555
LISTEN_ADDRESS = '0.0.0.0'

app = Flask(__name__)

def start(host=LISTEN_ADDRESS, port=PORT, use_debugger=True):
  """Start Smashery Proxy"""
  print "Start Smashery Proxy"
  port = int(port)

  # Load config etc.

  app.secret = "A0Zr98j/3yX R~XHH!jmN"

  print app.url_map
  app.run(host, port, use_debugger)


@app.route('/<service>/<endpoint>/')
def v2_dispatch(service, enpoint):
  print "AIYEEEE"
  if service not in settings['service_map']:

    abort(404)
  
  proxy_target  = settings['target_url']
  proxy_service = settings['service_map'][service]
  proxy_url = '/'.join([proxy_target, proxy_service, endpoint])
  print "Remapping to: %s" % proxy_url
  internal = requests.get(proxy_url)
  return r.text


if __name__ == "__main__":
  start()