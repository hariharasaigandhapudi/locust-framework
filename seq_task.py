from locust import HttpUser,task,SequentialTaskSet,constant


class seq_tasks(SequentialTaskSet):
    @task
    def get_posts(self):
        res=self.client.get("/api/users/2")
        print("Get Method Status is: ", res.status_code)

    @task
    def post_details(self):
       res = self.client.post("/api/users")
       print("Post Method Status is: ", res.status_code)

class myseq_set(HttpUser):
    wait_time = constant(1)
    host="https://reqres.in"

    tasks = [seq_tasks]

#run with "locust -f <filename> -u <usercount> -r <spawn count> -t <time to execute> -- headless --html=<filename>.html"
