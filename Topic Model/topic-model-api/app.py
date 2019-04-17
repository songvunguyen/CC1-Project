#https://medium.com/octopus-labs-london/how-to-build-a-rest-api-in-python-with-tornado-fc717c33824a
#https://medium.com/octopus-labs-london/how-to-build-a-rest-api-in-python-with-tornado-part-2-8ebc423bd4fa
#https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
import sys
import numpy
sys.path.append('/Users/Gtt/Desktop/CC1-Project/Topic Model')
from api import *
from urllib.parse import *
topics = []

class QueryHandler(RequestHandler):
  def get(self):
    self.write({'topics': topics})

class ListTopics(RequestHandler):
  def post(self):
    global topics
    text = self.request.body
    text = json.loads(text)
    output = query(str(text['text']))
    for i in output:
      topics.append(json.loads(json.dumps(i)))
    
    self.write({'topics': topics})

def make_app():
  urls = [("/", QueryHandler),("/api/topics", ListTopics)]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(9000)
    IOLoop.instance().start()