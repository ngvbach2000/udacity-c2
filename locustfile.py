from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 4.0)

    @task(1)
    def test(self):
        self.client.post("https://udacity-c2.scm.azurewebsites.net/")
