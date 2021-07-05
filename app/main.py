import json
from flask import Flask, request
import requests
from healthcheck import HealthCheck
app = Flask(__name__)
app.config["DEBUG"] = True
#for checking health of api service
health = HealthCheck()
def redis_available():
    return True, "UP"

health.add_check(redis_available)

app.add_url_rule("/health", "healthcheck", view_func=lambda: health.run())

#for creating ping service
@app.route('/api/v1/ping',methods=['POST'])
def api_v1_ping():
    #to fetch the data from post request and parse the data
    data=json.loads(request.get_data())
    # print(data)
    #fetching the url in json payload
    url = data['url']
    #sending request to url
    response=requests.get("{}".format(url))
    # print(response.text)
    #reciving payload fro url
    pay_load= response.text
    return pay_load

#RECEIVER SERVICE
@app.route('/api/v1/info',methods=['GET'])
def api_v1_info():
    data={"Receiver":"Cisco is the best"}
    #sending data to the get service
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True,port=8080)

