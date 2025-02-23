# all tasks only have two status : open , finished
class Task:
    def __init__(self, taskname):
        self.taskname = taskname
        self.status = "open"
    def change(self):
        if self.status == "open":
            self.status = "finished"
        else :
            self.status = "open"
    def __str__(self):
        return self.taskname
    

