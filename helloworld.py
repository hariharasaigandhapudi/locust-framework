from locust import User,task,constant


class MyUser(User):
    wait_time = constant(1)

    @task
    def say_hello(self):
        print("hello world")

    @task
    def weak_mask(self):
        print("Please wear mask")

    @task
    def say_goodbye(self):
        print("Good Bye!")
    