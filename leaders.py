class Leader:
    def __init__(self,first_name,last_name,form,rank):
        self.first_name = first_name
        self.last_name = last_name
        self.form = form
        self.rank = rank
    def __str__(self):
        return f'{self.first_name} {self.last_name} form {self.form}: {self.rank}'
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
leader1=Leader