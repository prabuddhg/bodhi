# borrowed from https://github.com/aranaea/kafka-demo/blob/master/producer/src/app.py
from flask import Flask, request
import json
import lib.poisson as poisson
from lib.publisher import Publisher
import time
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

dispatcher = Publisher(logging) #TODO: There's probably a better way to encapsulate logging

@app.route("/")
def index():
    return "This is job trigger, please use /startjobs to trigger all the jobs"

@app.route("/startjobs", methods=['POST'])
def post_event():
   arrival_interval = 0
   for num in range(0,13):
       arrival_interval = arrival_interval + poisson.next_arrival_time()*10
       time.sleep(arrival_interval)
       app.logger.debug("Job ID: workload-%s produced at %s seconds" %(num,
             int(arrival_interval)))

       #message = request.get_json()
       message = "schedule : workload-%s" %num 
       app.logger.debug("request had the following data: {0}".format(message))
       #dispatcher.push(message)
       
   return json.dumps({'status': 'success', 'response_data': message}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
