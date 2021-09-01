
import time
import json
from locust import HttpUser, task, between


test_data = json.dumps({ 'data': [["I love this phone , It is very handy and has a lot of features ."]]})
headers = {'Content-Type': 'application/json'}


class MLServiceUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_nlp_predictions(self):
        self.client.post("http://ac6b05fa-e01f-4ef3-ad1f-ee83bd208396.centralus.azurecontainer.io/score", data=test_data, headers=headers)
