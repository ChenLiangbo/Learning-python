#!/user/bin/env/python
#coding:utf-8

from locust import HttpLocust, TaskSet, task
import subprocess

# Web API ability test  alertapp/tornado-server
class UserBehavior(TaskSet):

    def on_start(self):

        """ on_start is called when a Locust start before any task is scheduled """

        self.login()

 
    def login(self):
        self.client.get("/login/")

 

    @task(2)
    def login_post(self):
        self.client.post("/login/",{"username":"justin","password":"hk1688"})

    # @task(1)
    # def stations(self):

    #     self.client.get("/stations/?name=u'虹口站'",)

class WebsiteUser(HttpLocust):

    task_set = UserBehavior

    min_wait=5000

    max_wait=15000

    host = 'http://192.168.1.42:5656'  # url = http://host:port



# run this demo
# locust -f locust_server_test.py

# if __name__ == '__main__':
#    subprocess.Popen('locust -f locust_server_test.py', shell=True)